import unittest
import ConvertListToDict as cldf

class MyDictTestCase(unittest.TestCase):
    def test_Dict(self):
        # Testcase1 (len(keys) == len(values))
        actualDict1 = cldf.ConvertListsToDict([1, 2, 3],['a','b','c'])
        expectedDict1 = {1: 'a', 2: 'b', 3: 'c'}
        self.assertEqual(actualDict1, expectedDict1)

        # Testcase2 (len(keys) < len(values))
        actualDict2 = cldf.ConvertListsToDict([1, 2, 3], ['a', 'b', 'c','d','e','f'])
        expectedDict2 = {1: 'a', 2: 'b', 3: 'c'}
        self.assertEqual(actualDict2, expectedDict2)

        # Testcase3 (len(keys) > len(values))
        actualDict2 = cldf.ConvertListsToDict([1, 2, 3, 4, 5, 6, 7], ['a', 'b', 'c'])
        expectedDict2 = {1: 'a', 2: 'b', 3: 'c', 4: None, 5: None, 6: None, 7: None}
        self.assertEqual(actualDict2, expectedDict2)


if __name__ == '__main__':
    unittest.main()
