import unittest
from typing import Dict

from filewordcounter.counter import Counter


class CounterTest(unittest.TestCase):

    def testForCorrectOutput(self):
        path, formats, count = Counter.parse_input('input.txt')
        counter = Counter(path, formats, count)
        res: Dict[str, int] = counter.walk()
        self.assertEqual(res['README.md'], 930)

    def testWithTestInput(self):
        path, formats, count = Counter.parse_input('test-input1.txt')
        counter = Counter(path, formats, count)
        res: Dict[str, int] = counter.walk()
        self.assertEqual(res['Fibonacci.java'], 86)
        self.assertEqual(res['Palindrome.java'], 47)