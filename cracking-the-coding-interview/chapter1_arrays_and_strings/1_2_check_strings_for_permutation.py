import unittest


def is_permutation(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    return set(str1) == set(str2)  # todo: why isn't it reference comparison?


class PermutationsTest(unittest.TestCase):

    def test_is_permutation(self):
        self.assertTrue(is_permutation("abc", "cab"))
        self.assertTrue(is_permutation("abcd", "dcab"))


if __name__ == "__main__":
    unittest.main()
