import unittest

from solution import Autocomplete, Node


class SolutionTest(unittest.TestCase):

    def testForCorrectOutput(self):
        auto = Autocomplete(*Autocomplete.parse_input('input.txt'))
        tree: Node = auto.build_prefix_tree(auto.dictionary)
        res = auto.search_in_tree(tree, "catc")
        self.assertEqual(res[0], "catch (10)")
