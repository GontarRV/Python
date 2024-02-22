import unittest
from UFO import UFO

class UFOTests(unittest.TestCase):

    def tests_basic_true(self):
        self.assertEqual(UFO(2, [1234, 1777], True), [668, 1023])

    def tests_basic_false(self):
        self.assertEqual(UFO(2, [1234, 1777], False), [4660, 6007])

    def tests_many_num(self):
        self.assertEqual(UFO(10, [12345, 66545, 7446, 125457, 32145, 63521,
                                  4512324, 45156, 45615, 65154], True), [5349,
                                  28005, 3878, 43823, 13413, 26449, 1217748, 
                                  19054, 19341, 27244])
    def tests_big_num(self):
        self.assertEqual(UFO(3, [1111111111, 123456123, 12456451235], False), 
                         [73300775185, 4886716707, 1255577817653])
        
if __name__ == '__main__':
    unittest.main()