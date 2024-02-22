import unittest
from MassVote import MassVote

class MassVoteTests(unittest.TestCase):

    def tests_many_votes(self):
        self.assertEqual(MassVote(4, [100000, 99999, 2000, 5001]), 'no winner')

    def tests_big_vote(self):
        self.assertEqual(MassVote(5, [25, 50, 100, 15, 10]), 'majority winner 3')

    def tests_small_vote(self):
        self.assertEqual(MassVote(10, [10, 15, 30, 5, 10, 20, 40, 25, 35, 15]), 'minority winner 7')

if __name__ == '__main__':
    unittest.main()