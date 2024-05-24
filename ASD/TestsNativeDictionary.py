import unittest
from NativeDictionary import NativeDictionary


class TestNativeDictionary(unittest.TestCase):
    def test_hash_fun(self):
        table = NativeDictionary(10)
        self.assertTrue(table.hash_fun("aaa") < table.size)
        self.assertTrue(
            table.hash_fun("aaaabbbcccddddeee12345") < table.size)
        self.assertTrue(table.hash_fun(
            "aaaabbbcccddddeee12345") < table.size)
        self.assertTrue(table.hash_fun("12345") < table.size)
        self.assertTrue(table.hash_fun("b") < table.size)
        self.assertTrue(table.hash_fun("c") < table.size)

    def test_is_key(self):
        table = NativeDictionary(5)
        table.slots[0] = "a"
        table.values[0] = "aaa"
        table.slots[2] = "b"
        table.values[2] = "bbb"
        self.assertTrue(table.is_key("a"))
        self.assertFalse(table.is_key("c"))

    def test_put(self):
        table = NativeDictionary(5)
        table.put("a", "aaa")
        table.put("b", "bbb")
        table.put("c", "ccc")
        self.assertTrue(table.is_key("a"))
        self.assertTrue(table.is_key("b"))
        self.assertTrue(table.is_key("c"))
        self.assertEqual(table.put("a", "d"), None)

    def test_get(self):
        table = NativeDictionary(3)
        table.put("a", "aaa")
        table.put("b", "bbb")
        table.put("c", "ccc")
        self.assertEqual(table.get("a"), "aaa")
        self.assertEqual(table.get("b"), "bbb")
        self.assertEqual(table.get("c"), "ccc")

        table.put("a", "abcba")
        self.assertEqual(table.get("a"), "abcba")
        self.assertEqual(table.get("d"), None)


if __name__ == '__main__':
    unittest.main()
