def validate_dna_sequence(sequence: str) -> bool:
    return all(nucleotide in 'ATCG' for nucleotide in sequence.upper())
