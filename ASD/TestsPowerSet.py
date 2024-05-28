import unittest
from powerset import PowerSet


class TestPowerSet(TestCase):
    def test_size(self):
        powerset = PowerSet()
        self.assertEqual(0, powerset.size())
        self.assertFalse(powerset.remove(10))
        self.assertEqual(0, powerset.size())

        self.assertEqual(10, powerset.put(10))
        self.assertEqual(1, powerset.size())

        self.assertEqual(20, powerset.put(20))
        self.assertEqual(2, powerset.size())

        self.assertEqual(30, powerset.put(30))
        self.assertEqual(3, powerset.size())

        self.assertTrue(powerset.remove(20))
        self.assertEqual(2, powerset.size())

    def test_put(self):
        powerset = PowerSet()
        self.assertEqual(0, powerset.size())
        self.assertEqual(10, powerset.put(10))
        self.assertEqual(20, powerset.put(20))
        self.assertEqual(30, powerset.put(30))
        self.assertEqual(3, powerset.size())

        self.assertEqual(10, powerset.put(10))
        self.assertEqual(20, powerset.put(20))
        self.assertEqual(3, powerset.size())

        self.assertEqual(40, powerset.put(40))
        self.assertEqual(4, powerset.size())

    def test_get(self):
        powerset = PowerSet()
        self.assertFalse(powerset.get(10))
        self.assertFalse(powerset.get(20))
        self.assertFalse(powerset.get(30))

        self.assertEqual(10, powerset.put(10))
        self.assertTrue(powerset.get(10))
        self.assertFalse(powerset.get(20))
        self.assertFalse(powerset.get(30))

        self.assertEqual(20, powerset.put(20))
        self.assertEqual(30, powerset.put(30))
        self.assertTrue(powerset.get(10))
        self.assertTrue(powerset.get(20))
        self.assertTrue(powerset.get(30))

    def test_remove(self):
        powerset = PowerSet()
        self.assertEqual(0, powerset.size())
        self.assertFalse(powerset.remove(10))
        self.assertEqual(0, powerset.size())

        self.assertEqual(10, powerset.put(10))
        self.assertEqual(1, powerset.size())

        self.assertEqual(20, powerset.put(20))
        self.assertEqual(2, powerset.size())

        self.assertTrue(powerset.remove(10))
        self.assertEqual(1, powerset.size())
        self.assertFalse(powerset.get(10))
        self.assertTrue(powerset.get(20))

    def test_intersection(self):
        r1 = PowerSet()
        for number in [10, 20, 30, 40, 50]:
            r1.put(number)

        r2 = PowerSet()
        for number in [30, 40, 50, 60, 70]:
            r2.put(number)

        r3 = PowerSet()
        for number in [60, 70, 80]:
            r3.put(number)

        intersection_set = r1.intersection(r2)
        self.assertEqual(3, intersection_set.size())
        self.assertFalse(intersection_set.get(10))
        self.assertFalse(intersection_set.get(20))
        self.assertTrue(intersection_set.get(30))
        self.assertTrue(intersection_set.get(40))
        self.assertTrue(intersection_set.get(50))
        self.assertFalse(intersection_set.get(60))
        self.assertFalse(intersection_set.get(70))

        self.assertEqual(0, r1.intersection(r3).size())
        self.assertEqual(2, r2.intersection(r3).size())

    def test_union(self):
        r1 = PowerSet()
        for number in [10, 20, 30, 40, 50]:
            r1.put(number)

        r2 = PowerSet()
        for number in [30, 40, 50, 60, 70]:
            r2.put(number)

        union_set = r1.union(r2)
        self.assertEqual(7, union_set.size())
        self.assertTrue(union_set.get(10))
        self.assertTrue(union_set.get(20))
        self.assertTrue(union_set.get(30))
        self.assertTrue(union_set.get(40))
        self.assertTrue(union_set.get(50))
        self.assertTrue(union_set.get(60))
        self.assertTrue(union_set.get(70))

        self.assertEqual(5, r1.union(PowerSet()).size())

    def test_difference(self):
        r1 = PowerSet()
        for number in [10, 20, 30, 40, 50]:
            r1.put(number)

        r2 = PowerSet()
        for number in [30, 40, 50, 60, 70]:
            r2.put(number)

        r3 = PowerSet()
        for number in [0, 10, 20, 30, 40, 50, 60]:
            r3.put(number)

        difference_set = r1.difference(r2)
        self.assertEqual(2, difference_set.size())
        self.assertTrue(difference_set.get(10))
        self.assertTrue(difference_set.get(20))

        self.assertEqual(0, r1.difference(r3).size())
        self.assertEqual(1, r2.difference(r3).size())

    def test_issubset(self):
        r1 = PowerSet()
        for number in [10, 20, 30, 40, 50]:
            r1.put(number)
        self.assertTrue(r1.issubset(PowerSet()))

        r2 = PowerSet()
        for number in [30, 40, 50, 60, 70]:
            r2.put(number)
        self.assertFalse(r1.issubset(r2))

        r3 = PowerSet()
        for number in [30, 40, 50, 60]:
            r3.put(number)
        self.assertFalse(r1.issubset(r3))
        self.assertTrue(r2.issubset(r3))

        r4 = PowerSet()
        for number in [10, 20, 30, 40, 50, 60, 70]:
            r4.put(number)
        self.assertFalse(r1.issubset(r4))

if __name__ = "__main__":
    unittest.main()
 