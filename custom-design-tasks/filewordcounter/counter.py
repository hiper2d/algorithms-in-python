import os
from typing import Tuple, List, Dict


class Counter:
    def __init__(self, path_to_scan: str, supported_formats: List[str], word_limit: int):
        self.path_to_scan: str = path_to_scan
        self.supported_formats: List[str] = supported_formats
        self.word_limit: int = word_limit

    def walk(self) -> Dict[str, int]:
        res: Dict[str, int] = {}
        for (root, dirs, files) in os.walk(self.path_to_scan, topdown=True):
            for filename in files:
                _, ext = os.path.splitext(filename)
                if self.is_extension_in_input_list(ext):
                    word_count = self.count_words_in_file(filename, root)
                    if word_count >= self.word_limit:
                        res[filename] = word_count
        return res

    def is_extension_in_input_list(self, ext: str) -> bool:
        return ext and ext.startswith(".") and ext[1:] in self.supported_formats

    @staticmethod
    def count_words_in_file(filename: str, path: str) -> int:
        with open(path + "/" + filename) as f:
            read_data = f.read()
            per_word = read_data.split()
            return len(per_word)

    @staticmethod
    def parse_input(path: str) -> Tuple[str, List[str], int]:
        with open(path) as f:
            path_to_scan = f.readline().strip()
            supported_formats = f.readline().strip().split()
            word_limit = int(f.readline())
            return path_to_scan, supported_formats, word_limit


if __name__ == "__main__":
    counter = Counter(*Counter.parse_input('input.txt'))
    print(counter.walk())

