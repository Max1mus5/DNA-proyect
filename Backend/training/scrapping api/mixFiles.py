import pandas as pd

def mix_csv_files(genome_file, disease_file, output_file):
    """
    Combina los archivos genome.csv y disease.csv para crear genomeTrainDisease.csv.

    Args:
      genome_file (str): Ruta al archivo genome.csv
      disease_file (str): Ruta al archivo disease.csv
      output_file (str): Ruta al archivo de salida genomeTrainDisease.csv
    """
    # Cargar los archivos CSV con pandas
    genome_df = pd.read_csv(genome_file)
    disease_df = pd.read_csv(disease_file)

    #  Combinar los DataFrames utilizando 'rsid' y 'genotype' como claves
    merged_df = genome_df.merge(disease_df, on=['rsid', 'genotype'], how='left')

    # Reordenar las columnas para que coincidan con el formato de salida deseado
    merged_df = merged_df[[
        "rsid", "chromosome", "position", "genotype", 
        "magnitude", "reputation", "summary"
    ]]

    #  Llenar los valores NaN con cadenas vacías
    merged_df.fillna("", inplace=True)

    # Guardar el DataFrame combinado en un nuevo archivo CSV
    merged_df.to_csv(output_file, index=False)

    print(f"Archivo {output_file} creado exitosamente.")

# Ejecutar la función
mix_csv_files('training\genome.csv', 'training\disease.csv', 'training\genomeTrainDisease.csv')