from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'T', 'G', 'C'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Tuple]

gene_str = "ATGCGCTAGCTAGCTAGCTAGCATATATCGATCAGCTACGATCAGCTACGATCGATGCATGCATGCTAGCATGCATGCATGCTAGCATGCATGCAT"


def string_to_gene(g_str: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(g_str), 3):
        if i + 2 > len(g_str):
            return gene
        codon: Codon = (Nucleotide[g_str[i]], Nucleotide[g_str[i+1]], Nucleotide[g_str[i+2]])
        gene.append(codon)
    return gene


def linear_search(g: Gene, conon: Codon) -> bool:
    for c in g:
        if c == conon:
            return True
    return False


if __name__ == "__main__":
    gene: Gene = string_to_gene(gene_str)
    codon_agg = (Nucleotide.A, Nucleotide.G, Nucleotide.G)
    print(linear_search(gene, codon_agg))
