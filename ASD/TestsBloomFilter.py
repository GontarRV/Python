import unittest

from BloomFilter import BloomFilter

strtest = {'str1': "0123456789",
           'str2': "1234567890",
           'str3': "2345678901",
           'str4': "3456789012",
           'str5': "4567890123",
           'str6': "5678901234",
           'str7': "6789012345",
           'str8': "7890123456",
           'str9': "8901234567",
           'str10': "9012345678"}

class TestBloomFilter(unittest.TestCase):

    def setUp(self):
        self.m = 32
        self.Bloom = BloomFilter(self.m)

    def test_empty_filter(self):
        for i in strtest.keys():
            self.assertFalse(self.Bloom.is_value(strtest[i]))

    def test_full_filter(self):
        for i in strtest.keys():
            self.Bloom.add(strtest[i])

        for i in strtest.keys():
            self.assertTrue(self.Bloom.is_value(strtest[i]))

if __name__ == '__main__':
    unittest.main()