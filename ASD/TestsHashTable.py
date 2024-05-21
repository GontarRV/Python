import unittest

from HashTable import HashTable

class TestHashTable(unittest.TestCase):
    def test_constructor(self):
        hash_table = HashTable(11, 2)
        self.assertEqual(hash_table.size, 11)
        self.assertEqual(hash_table.step, 2)
        self.assertEqual(len(hash_table.slots), 11)
        self.assertTrue(all([slot is None for slot in hash_table.slots]))

    def test_hash_fun(self):
        hash_table = HashTable(11, 2)
        test_data = ['qwertyuiopasdfghj',
            'aaaaaaaaaaaaaaa',
            '1234567890ASDFGHJKLLQWERTY',
            '                        ']
        for test_case in test_data:
            self.assertIsInstance(hash_table.hash_fun(test_case), int)
            self.assertGreaterEqual(hash_table.hash_fun(test_case), 0)
            self.assertLess(hash_table.hash_fun(test_case), hash_table.size)

    def test_seek_slot(self):
        hash_table = HashTable(11, 2)
        value = 'aaa'
        for i in range(10):
            hash_table.slots[i] = value
        self.assertEqual(hash_table.seek_slot(value), 10)
        hash_table.slots[10] = value
        self.assertIsNone(hash_table.seek_slot(value + value))

    def test_find(self):
        hash_table = HashTable(11, 2)
        self.assertIsNone(hash_table.find('value'))

    def test_put(self):
        hash_table = HashTable(11, 2)
        value = 'aaaagaergerge123456'
        self.assertIsNone(hash_table.find(value))
        hash_table.put(value)
        self.assertEqual(hash_table.find(value), hash_table.hash_fun(value))

    def test_hash_fun_1(self):
        chart = HashTable(11, 2)
        self.assertTrue(chart.hash_fun("aaa") < chart.size)
        self.assertTrue(chart.hash_fun("aaaagaergerge123456") < chart.size)
        self.assertTrue(chart.hash_fun("aaaagaergerge123456") < chart.size)
        self.assertTrue(chart.hash_fun("12345") < chart.size)
        self.assertTrue(chart.hash_fun("c") < chart.size)
        self.assertTrue(chart.hash_fun("b") < chart.size)

    def test_seek_slot_1(self):
        chart = HashTable(11, 3)
        chart.slots[0] = "a"
        chart.slots[1] = "a"
        chart.slots[2] = "a"
        chart.slots[3] = "a"
        chart.slots[5] = "a"
        chart.slots[6] = "a"
        chart.slots[7] = "a"
        chart.slots[8] = "a"
        chart.slots[9] = "a"
        chart.slots[10] = "a"
        self.assertEqual(chart.seek_slot("c"), 4)
        chart.slots[4] = "a"
        self.assertEqual(chart.seek_slot("c"), None)

        chart = HashTable(11, 3)
        chart.slots[0] = "a"
        chart.slots[2] = "a"
        chart.slots[3] = "a"
        chart.slots[4] = "a"
        chart.slots[5] = "a"
        chart.slots[6] = "a"
        chart.slots[7] = "a"
        chart.slots[8] = "a"
        chart.slots[9] = "a"
        chart.slots[10] = "a"
        self.assertEqual(chart.seek_slot("b"), 1)

    def test_put_1(self):
        chart = HashTable(11, 2)
        for c in "abcdefhijkl":
            self.assertIsNotNone(chart.put(c))

        self.assertIsNone(chart.put("safasf"))

    def test_find_1(self):
        chart = HashTable(11, 2)
        for c in "abcdefhijkl":
            chart.put(c)

        self.assertIsNotNone(chart.find("l"))
        self.assertIsNone(chart.find("oo"))


if __name__ == '__main__':
    unittest.main()

