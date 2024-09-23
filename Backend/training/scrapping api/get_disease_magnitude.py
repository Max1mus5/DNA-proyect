import asyncio
import aiohttp
import pandas as pd
from bs4 import BeautifulSoup

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

    # Convertir el genotipo al formato "A;A" (o similar)
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
