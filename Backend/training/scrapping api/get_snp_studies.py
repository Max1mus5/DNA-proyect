import aiohttp
import asyncio
import csv
import re
from bs4 import BeautifulSoup
from aiohttp import TCPConnector

# URL base para consultas a SNPedia
BASE_URL = "https://www.snpedia.com/index.php?title=Special:Ask&limit=500&offset={offset}&q=%5B%5BCategory%3AIs+a+genotype%5D%5D&p=mainlabel%3D%2Fformat%3Dtable&po=%3FMagnitude%0A%3FRepute%0A%3FSummary%0A&sort=Magnitude&order=desc&eq=no#search"

# Archivo de salida
OUTPUT_FILE = '..\disease.csv'

# Encabezados del CSV
CSV_HEADERS = ["rsid", "genotype", "magnitude", "reputation", "summary"]

# Función para analizar una fila de la tabla y extraer los datos
def parse_row(row):
    try:
        cells = row.find_all("td")
        
        # Extraer rsid y genotipo
        rsid_genotype = cells[0].find("a").get("title")
        match = re.match(r'([^()]+)\(([^)]+)\)', rsid_genotype)
        if match:
            rsid, genotype = match.groups()
        else:
            rsid, genotype = None, None
        rsid = rsid.lower() if rsid else "none"
        genotype = genotype.replace(";", "") if genotype else "none"

        # Extraer los demás campos utilizando una comprensión de lista
        magnitude, reputation, summary = [
            cell.text.strip() if cell.text.strip() else default 
            for cell, default in zip(cells[1:], ["1", "", ""])
        ]

    except Exception as e:
        print(f"Error parsing row: {e}")
        rsid = "none"
        genotype = "none"
        magnitude = "1"
        reputation = ""
        summary = ""

    return {
        "rsid": rsid,
        "genotype": genotype,
        "magnitude": magnitude,
        "reputation": reputation,
        "summary": summary
    }

# Función para hacer la solicitud y procesar los resultados
async def fetch_snp_data(session, offset):
    url = BASE_URL.format(offset=offset)
    try:
        print(f"Fetching data from {url}...")
        async with session.get(url) as response: 
            page_content = await response.text()
            soup = BeautifulSoup(page_content, 'html.parser')

            # Buscar las filas de la tabla utilizando un selector CSS
            rows = soup.select("tr[class^=row-]")

            # Utilizar una comprensión de lista para obtener los datos de cada fila
            snp_data = [parse_row(row) for row in rows]

            return snp_data
    except Exception as e:
        print(f"Error fetching data for offset {offset}: {e}")
        return [] 

# Función principal para gestionar múltiples solicitudes
async def gather_snp_data():
    print("Iniciando solicitudes asincrónicas...")
    offsets = range(0, 5500, 500) 
    
    # Crear un conector TCP que ignore SSL (no recomendado en producción)
    connector = TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [fetch_snp_data(session, offset) for offset in offsets]
        all_data = await asyncio.gather(*tasks)

        # Aplanar la lista de listas utilizando una comprensión de lista
        snp_data = [item for sublist in all_data for item in sublist]

        # Escribir los datos en un archivo CSV
        with open(OUTPUT_FILE, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=CSV_HEADERS)
            writer.writeheader()
            writer.writerows(snp_data)

        print(f"Datos guardados en {OUTPUT_FILE}")

print("Iniciando procesamiento de datos de SNPedia...")
asyncio.run(gather_snp_data())
print("Procesamiento de datos de SNPedia completado exitosamente.")