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


def contains_linear(g: Gene, codon: Codon) -> bool:
    for c in g:
        if c == codon:
            return True
    return False


def contains_binary(g: Gene, codon: Codon) -> bool:
    low = 0
    high = len(g) - 1
    while True:
        if low >= high:
            return False
        mid = (high + low) // 2
        if g[mid] > codon:
            low = mid + 1
        elif g[mid] < codon:
            high = mid - 1
        else:
            return True


if __name__ == "__main__":
    gene: Gene = string_to_gene(gene_str)
    print(contains_linear(gene, (Nucleotide.A, Nucleotide.G, Nucleotide.G)))
    gene_sorted = sorted(gene)
    print(contains_binary(gene, (Nucleotide.C, Nucleotide.G, Nucleotide.C)))
