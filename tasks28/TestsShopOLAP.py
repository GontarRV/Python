import unittest
from ShopOLAP import ShopOLAP

class TestsShopOLAP(unittest.TestCase):

    def tests_one(self):
        self.assertEqual(ShopOLAP(5, ['платье 3', 'сумка1 4', 'сумка123 2', 'сумка 1', 'сумка2 3']),
                         ['платье 3', 'сумка 1', 'сумка1 4', 'сумка123 2', 'сумка2 3'])

    def tests_two(self):
        self.assertEqual(ShopOLAP(5, ['платье1 5', 'сумка32 2', 'платье1 1', 'сумка23 2', 'сумка128 4']),
                         ['платье1 6', 'сумка128 4', 'сумка23 2', 'сумка32 2'])
        
if __name__ == '__main__':
    unittest.main()