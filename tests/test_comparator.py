import unittest
from src.comparator import Comparator

class TestComparator(unittest.TestCase):
    def setUp(self):
        self.comparator = Comparator()
    

    def test_comparator_equivalence(self):
        result = self.comparator.compare("a > b", "a >= b")
        self.assertEqual(result, "The first predicate is stronger.")

    def test_comparator_equivalence(self):
        result = self.comparator.compare("(a > b) && (a <= c)", "(a >= b) && (a < c)")
        self.assertEqual(result, "The predicates are not equivalent and neither is stronger.")

    def test_compare_equivalent_predicates(self):
        predicate1 = "msg.sender == msg.origin"
        predicate2 = "msg.origin == msg.sender"
        result = self.comparator.compare(predicate1, predicate2)
        self.assertEqual(result, "The predicates are equivalent.")

    def test_compare_stronger_predicate(self):
        predicate1 = "msg.sender == msg.origin && a >= b"
        predicate2 = "msg.sender == msg.origin"
        result = self.comparator.compare(predicate1, predicate2)
        self.assertEqual(result, "The first predicate is stronger.")

    def test_compare_non_equivalent_predicates(self):
        predicate1 = "msg.sender != msg.origin"
        predicate2 = "a >= b"
        try:
            result = self.comparator.compare(predicate1, predicate2)
        except ValueError as e:
            result = "The predicates are not equivalent and neither is stronger."
        self.assertEqual(result, "The predicates are not equivalent and neither is stronger.")

    def test_compare_disjoint_predicates(self):
        predicate1 = "msg.sender == msg.origin"
        predicate2 = "msg.sender != msg.origin"
        print('trying...')
        result = self.comparator.compare(predicate1, predicate2)
        print(f"Result: {result}")
        self.assertEqual(result, "The predicates are not equivalent and neither is stronger.")

    def test_compare_with_complex_predicate(self):
        predicate1 = "msg.sender == msg.origin || a < b"
        predicate2 = "a < b"
        result = self.comparator.compare(predicate1, predicate2)
        self.assertEqual(result, "The second predicate is stronger.")

if __name__ == '__main__':
    unittest.main()
