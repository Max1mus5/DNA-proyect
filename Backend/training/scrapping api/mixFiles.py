import pandas as pd
import csv

def mix_csv_files(genome_file, disease_file, output_file):
    """
    Combina los archivos genome.csv y disease.csv para crear genomeTrainDisease.csv.

    Args:
    genome_file (str): Ruta al archivo genome.csv
    disease_file (str): Ruta al archivo disease.csv
    output_file (str): Ruta al archivo de salida genomeTrainDisease.csv
    """
    # Cargar los archivos CSV
    genome_df = pd.read_csv(genome_file)
    disease_df = pd.read_csv(disease_file)

    # Crear un diccionario para almacenar la información de disease.csv
    disease_dict = {}
    for _, row in disease_df.iterrows():
        key = (row['rsid'], row['genotype'])
        disease_dict[key] = {
            'magnitude': row['magnitude'],
            'reputation': row['reputation'],
            'summary': row['summary']
        }

    # Abrir el archivo de salida
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["rsid", "chromosome", "position", "genotype", "magnitude", "reputation", "summary"])
        count = 0
        # Iterar sobre las filas de genome.csv
        for _, row in genome_df.iterrows():
            rsid = row['rsid']
            genotype = row['genotype']
            key = (rsid, genotype)

            # Buscar coincidencias en el diccionario de disease
            if key in disease_dict:
                count += 1
                disease_info = disease_dict[key]
                writer.writerow([
                    rsid,
                    row['chromosome'],
                    row['position'],
                    genotype,
                    disease_info['magnitude'],
                    disease_info['reputation'],
                    disease_info['summary']
                ])
            else:
                # Si no hay coincidencia, escribir la fila con valores vacíos para magnitude, reputation y summary
                writer.writerow([
                    rsid,
                    row['chromosome'],
                    row['position'],
                    genotype,
                    "",
                    "",
                    ""
                ])
        print(f"Se han combinado {count} filas de genome.csv y disease.csv.")

    print(f"Archivo {output_file} creado exitosamente.")

# Ejecutar la función
mix_csv_files('training\genome.csv', 'training\disease.csv', 'training\genomeTrainDisease.csv')