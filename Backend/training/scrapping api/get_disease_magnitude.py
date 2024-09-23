import asyncio
import aiohttp
import pandas as pd
from bs4 import BeautifulSoup

def preprocess_genome_data(filepath):
    # Cargar el archivo genome.csv
    genome_data = pd.read_csv(filepath)

    # Asegurarse de que los genotipos estén en el formato adecuado "A;A"
    def format_genotype(genotype):
        return ';'.join(list(genotype))

    # Aplicar la transformación a los genotipos
    genome_data['genotype'] = genome_data['genotype'].apply(format_genotype)

    # Convertir rsid a mayúsculas
    genome_data['rsid'] = genome_data['rsid'].str.upper()

    return genome_data

async def fetch_snp_info(session, rsid, genotype):
    """
    segund el rsid y el genotipo, devuelve la magnitud y reputación de la enfermedad asociada

    Args:
    session (aiohttp.ClientSession): Sesión de aiohttp para realizar peticiones asíncronas.
    rsid (str): ID del SNP.
    genotype (str): Genotipo del SNP.

    Returns:
    dict: Diccionario con la magnitud y reputación de la enfermedad asociada.
    """

    # Convertir el genotipo al formato "A;A"
    genotype = genotype.replace('', ';')
    url = f"https://www.snpedia.com/index.php/{rsid}({genotype})"
    
    try:
        async with session.get(url) as response:
            if response.status != 200:
                print(f"Error fetching {rsid}: Status code {response.status}")
                return {'rsid': rsid, 'genotype': genotype, 'magnitude': -1, 'reputation': 'unmeasured'}

            page_content = await response.text()
            soup = BeautifulSoup(page_content, 'html.parser')

            # Verificar si la página no tiene información
            if soup.find('div', class_='noarticletext mw-content-ltr'):
                return {'rsid': rsid, 'genotype': genotype, 'magnitude': -1, 'reputation': 'unmeasured'}

            # Extraer magnitud
            try:
                magnitude = soup.find('a', {'title': 'Magnitude'}).find_next('td').text.strip()
            except AttributeError:
                magnitude = -1

            # Extraer reputación
            try:
                reputation = soup.find('a', {'title': 'Repute'}).find_next('td').text.strip()
            except AttributeError:
                reputation = 'unmeasured'

            return {'rsid': rsid, 'genotype': genotype, 'magnitude': magnitude, 'reputation': reputation}

    except Exception as e:
        print(f"Error fetching data for {rsid}: {e}")
        return {'rsid': rsid, 'genotype': genotype, 'magnitude': -1, 'reputation': 'unmeasured'}
    

async def process_snps_async(rsids_genotypes):
    results = []
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_snp_info(session, rsid, genotype) for rsid, genotype in rsids_genotypes]
        results = await asyncio.gather(*tasks)
    return results


 # Preprocesar los datos de genome.csv
genome_data = preprocess_genome_data('..\genome.csv')

# Crear una lista de tuplas (rsid, genotype)
rsids_genotypes = list(zip(genome_data['rsid'], genome_data['genotype']))

# Ejecutar las solicitudes asincrónicas
results = asyncio.run(process_snps_async(rsids_genotypes))

# Crear un DataFrame con los resultados
results_df = pd.DataFrame(results)

# Guardar los resultados en disease.csv
results_df.to_csv('disease.csv', index=False, columns=['rsid', 'genotype', 'magnitude', 'reputation'])
