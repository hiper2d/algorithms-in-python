import os
import re
import unittest


class WordCounter:

    @staticmethod
    def count():
        path = '/Users/hiper2d/projects/coroutines-playground/src/main/kotlin/com/hiper2d/basics/'
        print(os.listdir(path))

        words_count = 0
        with open(path + 'basics.kt') as f:
            lines = f.readlines()
            for l in lines:
                words = re.findall(r'\w+', l)
                words_count += len(words)
        return words_count


class WordCounterTest(unittest.TestCase):

    def testCount(self):
        self.assertEqual(141, WordCounter.count())


if __name__ == "__main__":
    print(WordCounter.count())
