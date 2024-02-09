import unittest
from SynchronizingTables import SynchronizingTables

class SynchronizingTablesTests(unittest.TestCase):

    def tests_simple(self):
        self.assertEqual(SynchronizingTables(3, [3,2,1],
                                             [400,800,500]),
                                             [800,500,400])

    def tests_repeated(self):
        self.assertEqual(SynchronizingTables(5, [7,4,9,11,3],
                                             [1000,1000,9000,5000,6000]),
                                             [5000,1000,6000,9000,1000])

    def tests_with_large_values(self):
        self.assertEqual(SynchronizingTables(4, [521,300,1002, 807],
                                             [10000, 50000, 23000, 1000000]),
                                             [23000,10000,1000000,50000])

if __name__ == '__main__':
    unittest.main()