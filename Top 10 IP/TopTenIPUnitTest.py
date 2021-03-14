import unittest
import TopTenIPAddr as ttia


class MyTopTenIPTestCase(unittest.TestCase):
    def test_top_ten_IP(self):
        # Testcase1
        actualTopTenIP1 = ttia.FindTop10IpAddr('access.log')
        expectedTopTenIP1 = [('66.249.73.135', 482), ('46.105.14.53', 364), ('130.237.218.86', 357), ('75.97.9.59', 273),
                            ('50.16.19.13', 113), ('209.85.238.199', 102), ('68.180.224.225', 99),
                            ('100.43.83.137', 84), ('208.115.111.72', 83), ('198.46.149.143', 82)]
        self.assertEqual( expectedTopTenIP1, actualTopTenIP1 )

        # Testcase2
        actualTopTenIP2 = ttia.FindTop10IpAddr('Test1AccessLog.txt')
        expectedTopTenIP2 = [('80.153.191.173', 6), ('67.61.162.49', 6), ('176.31.103.52', 6), ('50.131.51.216', 5),
                             ('207.241.237.104', 2), ('46.105.14.53', 2), ('180.180.119.57', 2), ('198.46.149.143', 2),
                             ('222.77.201.107', 2), ('119.63.196.16', 1)]
        self.assertEqual( expectedTopTenIP2, actualTopTenIP2 )


if __name__ == '__main__':
    unittest.main()
