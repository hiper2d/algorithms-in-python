#  Implement an algorithm to determine if a string has all unique characters.
#  What if you cannot use additional data structures?
import unittest


def is_unique(s: str) -> bool:
    return len(s) == len(set(s))


def is_unique_without_additional_data_structures(s: str) -> bool:
    s1 = list(s)
    s1.sort()  # better way is: ''.join(sorted(s))
    for i in range(1, len(s1)):
        if s1[i] == s1[i-1]:
            return False
    return True


class IsUniqueTest(unittest.TestCase):

    def test_is_unique(self):
        self.assertEqual(is_unique('sdfa'), True)
        self.assertEqual(is_unique('sdfass'), False)

    def test_is_unique_without_additional_data_structures(self):
        self.assertEqual(is_unique_without_additional_data_structures('sdfa'), True)
        self.assertEqual(is_unique_without_additional_data_structures('sdfass'), False)


if __name__ == "__main__":
    unittest.main()
