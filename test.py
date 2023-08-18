from unittest import TestCase, main

from whiteboard import solution

class MatchTestCase2(TestCase):
    def test_single_num(self):
        self.assertEqual(solution([6]),6)
    def test_single_zero(self):
        self.assertEqual(solution([0]), 0)
    def test_seven_zeros(self):
        self.assertEqual(solution([0,0,0,0,0,0,0]), 0)
    def test_one_two(self):
        self.assertEqual(solution([1,1,2]),2)
    def test_tripzero(self):
        self.assertEqual(solution([0,1,0,1,0]),0)
    def test_long(self):
        self.assertEqual(solution([1,2,2,3,3,3,4,3,3,3,2,2,1]),4)
    def test_longer(self):
        self.assertEqual(solution([1,1,2,2,3,3,3,6,6,3,2,2,2,2,2]),2)