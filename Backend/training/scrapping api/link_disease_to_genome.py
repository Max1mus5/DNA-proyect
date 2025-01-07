# link_disease_to_genome.py

import pandas as pd

def link_disease_to_genome(genome_file, disease_file, output_file):
    """
    Relaciona enfermedades a genomas en base a rsid y genotipo.

    Args:
      genome_file (str): Ruta al archivo CSV con información del genoma (rsid, genotipo, etc.).
      disease_file (str): Ruta al archivo CSV con información de enfermedades (rsid, genotipo, enfermedad).
      output_file (str): Ruta al archivo CSV de salida con la relación genoma-enfermedad.
    """

    # Cargar archivos CSV en DataFrames
    genome_df = pd.read_csv(genome_file)
    disease_df = pd.read_csv(disease_file)

    # Combinar DataFrames utilizando 'rsid' y 'genotype' como claves
    merged_df = pd.merge(genome_df, disease_df, on=['rsid', 'genotype'], how='left')

    # Guardar el DataFrame combinado en un nuevo archivo CSV
    merged_df.to_csv(output_file, index=False)

    print(f"Relación genoma-enfermedad guardada en {output_file}")