import unittest
from PrintingCosts import PrintingCosts

class PrintingCostsTests(unittest.TestCase):

    def tests_value_not_in_table(self):
        self.assertEqual(PrintingCosts('Проверка значения затраченного тонера'), 782)

    def tests_value_in_table(self):
        self.assertEqual(PrintingCosts('Checking the spent toner value'), 513)

    def tests_combined_values(self):
        self.assertEqual(PrintingCosts('Проверка потраченного toner value'), 643)

if __name__ == '__main__':
    unittest.main()