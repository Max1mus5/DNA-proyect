import aiohttp
import asyncio
import csv
import re
from bs4 import BeautifulSoup
import ssl
from aiohttp import TCPConnector

# URL base para consultas a SNPedia
BASE_URL = "https://www.snpedia.com/index.php?title=Special:Ask&limit=500&offset={offset}&q=%5B%5BCategory%3AIs+a+genotype%5D%5D&p=mainlabel%3D%2Fformat%3Dtable&po=%3FMagnitude%0A%3FRepute%0A%3FSummary%0A&sort=Magnitude&order=desc&eq=no#search"

# Archivo de salida
OUTPUT_FILE = '..\disease.csv'

# Encabezados del CSV
CSV_HEADERS = ["rsid", "genotype", "magnitude", "reputation", "summary"]

# Función para analizar una fila de la tabla y extraer los datos
def parse_row(row):
    cells = row.find_all("td")
    
    # Extraer rsid y genotipo
    rsid_genotype = cells[0].find("a").get("title")
    rsid, genotype = re.match(r'([^()]+)\(([^)]+)\)', rsid_genotype).groups()
    rsid = rsid.lower()
    genotype = genotype.replace(";", "")

    # Extraer los demás campos
    magnitude = cells[1].text.strip()
    reputation = cells[2].text.strip()
    summary = cells[3].text.strip()

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
    async with session.get(url, ssl=False) as response:  # Deshabilitamos SSL
        page_content = await response.text()
        soup = BeautifulSoup(page_content, 'html.parser')
        
        # Buscar las filas de la tabla
        rows = soup.find_all("tr", class_=re.compile(r"row-\w+"))

        snp_data = []
        for row in rows:
            snp_info = parse_row(row)
            snp_data.append(snp_info)

        return snp_data

# Función principal para gestionar múltiples solicitudes
async def gather_snp_data():
    offsets = range(0, 5000, 500)  # Desde offset 0 hasta 5000, de 500 en 500
    
    # Crear un conector TCP que ignore SSL
    sslcontext = ssl.create_default_context()
    sslcontext.check_hostname = False
    sslcontext.verify_mode = ssl.CERT_NONE

    connector = TCPConnector(ssl=sslcontext)
    
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [fetch_snp_data(session, offset) for offset in offsets]
        all_data = await asyncio.gather(*tasks)

        # Flatten the list of lists
        snp_data = [item for sublist in all_data for item in sublist]

        # Escribir los datos en un archivo CSV
        with open(OUTPUT_FILE, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=CSV_HEADERS)
            writer.writeheader()
            writer.writerows(snp_data)

        print(f"Datos guardados en {OUTPUT_FILE}")

asyncio.run(gather_snp_data())
