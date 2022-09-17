import unittest

from auto_complete.autocomplete import Trie, Autocomplete


class AutocompleteTest(unittest.TestCase):

    def test_add_word_to_trie(self):
        auto = Trie()
        word = "abc"
        auto.add(word)
        letter_index = 0
        curr = auto.root.children[word[letter_index]]
        while True:
            is_last_letter = True if letter_index == 2 else False
            self.assertEqual(is_last_letter, curr.is_word)
            letter_index += 1
            if len(curr.children) > 0:
                curr = curr.children[word[letter_index]]
            else:
                break

    def test_search_in_tree(self):
        auto = Autocomplete()
        auto.add_words_to_dictionary(["abc", "am", "abcd"])
        self.assertSetEqual(auto.autocomplete("ab"), {"abc", "abcd"})
