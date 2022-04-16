from sys import getsizeof


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str):
        self.bit_string: int = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide: {}".format(gene))

    def decompress(self) -> str:
        result = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            letter: int = self.bit_string >> i & 0b11
            if letter == 0b00:
                result += "A"
            elif letter == 0b01:
                result += "C"
            elif letter == 0b10:
                result += "G"
            elif letter == 0b11:
                result += "T"
            else:
                raise ValueError("Invalid code: {}".format(letter))
        return result[::-1]

    def __str__(self):
        return self.decompress()


if __name__ == "__main__":
    original = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    compressed: CompressedGene = CompressedGene(original)
    print("Original is {} bytes".format(getsizeof(original)))
    print("Compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print(compressed)
    print("Decompressed and Original are the same: {}".format(original == compressed.decompress()))
