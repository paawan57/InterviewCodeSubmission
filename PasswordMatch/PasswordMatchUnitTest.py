import unittest
import PasswordMatch as pm


class MyPassMatchTestCase(unittest.TestCase):
    def test_password_WithREMethod(self):
        # Testcase1 (len(password) == 0)
        actualPassValidity1 = pm.matchPasswordWithRE('')
        expectedPassValidity1 = "Invalid"
        self.assertEqual( expectedPassValidity1, actualPassValidity1 )

        # Testcase2 (len(password) > 20)
        actualPassValidity2 = pm.matchPasswordWithRE('Unds1dh..--dewhj...12234')
        expectedPassValidity2 = "Invalid"
        self.assertEqual( expectedPassValidity2, actualPassValidity2 )

        # Testcase3 (len(password) >=1 and len(password) <=20), characters in [a-zA-Z0-9.-]
        # starting with latin letter, Ending with latin letter
        actualPassValidity3 = pm.matchPasswordWithRE('PQE-234..--34d..sdf')
        expectedPassValidity3 = "Valid"
        self.assertEqual( expectedPassValidity3, actualPassValidity3 )

        # Testcase4 (len(password) >=1 and len(password) <=20), characters in [a-zA-Z0-9.-]
        # starting with latin letter, Ending with number
        actualPassValidity4 = pm.matchPasswordWithRE('Pfdf34...sd--f2345')
        expectedPassValidity4 = "Valid"
        self.assertEqual( expectedPassValidity4, actualPassValidity4 )

        # Testcase5 (len(password) >=1 and len(password) <=20), characters in [a-zA-Z0-9.-]
        # starting with number, Ending with number
        actualPassValidity5 = pm.matchPasswordWithRE('1dPfdf34...sd--f2345')
        expectedPassValidity5 = "Invalid"
        self.assertEqual( expectedPassValidity5, actualPassValidity5 )

        # Testcase6 (len(password) >=1 and len(password) <=20), characters in [a-zA-Z0-9.-]
        # starting with number, Ending with letter
        actualPassValidity6 = pm.matchPasswordWithRE('1dPfdf34...sd')
        expectedPassValidity6 = "Invalid"
        self.assertEqual( expectedPassValidity6, actualPassValidity6 )

        # Testcase7 (len(password) >=1 and len(password) <=20), characters in [a-zA-Z0-9.-]
        # starting or ending with chars [.,-]
        actualPassValidity7 = pm.matchPasswordWithRE('-dPfdf34...sd.')
        expectedPassValidity7 = "Invalid"
        self.assertEqual( expectedPassValidity7, actualPassValidity7 )

        # Testcase8 (len(password) >=1 and len(password) <=20), characters NOT IN [a-zA-Z0-9.-]
        actualPassValidity8 = pm.matchPasswordWithRE('dP*fdf---34...sd')
        expectedPassValidity8 = "Invalid"
        self.assertEqual( expectedPassValidity8, actualPassValidity8 )

    def test_password_WithoutREMethod(self):
        # Testcase1 (len(password) == 0)
        actualPassValidity1 = pm.matchPasswordWithoutRE('')
        expectedPassValidity1 = "Invalid"
        self.assertEqual(expectedPassValidity1, actualPassValidity1)

        # Testcase2 (len(password) > 20)
        actualPassValidity2 = pm.matchPasswordWithoutRE('Unds1dh..--dewhj...12234')
        expectedPassValidity2 = "Invalid"
        self.assertEqual(expectedPassValidity2, actualPassValidity2)

        # Testcase3 (len(password) >=1 and len(password) <=20), characters in [a-zA-Z0-9.-]
        # starting with latin letter, Ending with latin letter
        actualPassValidity3 = pm.matchPasswordWithoutRE('PQE-234..--34d..sdf')
        expectedPassValidity3 = "Valid"
        self.assertEqual(expectedPassValidity3, actualPassValidity3)

        # Testcase4 (len(password) >=1 and len(password) <=20), characters in [a-zA-Z0-9.-]
        # starting with latin letter, Ending with number
        actualPassValidity4 = pm.matchPasswordWithoutRE('Pfdf34...sd--f2345')
        expectedPassValidity4 = "Valid"
        self.assertEqual(expectedPassValidity4, actualPassValidity4)

        # Testcase5 (len(password) >=1 and len(password) <=20), characters in [a-zA-Z0-9.-]
        # starting with number, Ending with number
        actualPassValidity5 = pm.matchPasswordWithoutRE('1dPfdf34...sd--f2345')
        expectedPassValidity5 = "Invalid"
        self.assertEqual(expectedPassValidity5, actualPassValidity5)

        # Testcase6 (len(password) >=1 and len(password) <=20), characters in [a-zA-Z0-9.-]
        # starting with number, Ending with letter
        actualPassValidity6 = pm.matchPasswordWithoutRE('1dPfdf34...sd')
        expectedPassValidity6 = "Invalid"
        self.assertEqual(expectedPassValidity6, actualPassValidity6)

        # Testcase7 (len(password) >=1 and len(password) <=20), characters in [a-zA-Z0-9.-]
        # starting or ending with chars [.,-]
        actualPassValidity7 = pm.matchPasswordWithoutRE('-dPfdf34...sd.')
        expectedPassValidity7 = "Invalid"
        self.assertEqual(expectedPassValidity7, actualPassValidity7)

        # Testcase8 (len(password) >=1 and len(password) <=20), characters NOT IN [a-zA-Z0-9.-]
        actualPassValidity8 = pm.matchPasswordWithoutRE('dP*fdf---34...sd')
        expectedPassValidity8 = "Invalid"
        self.assertEqual(expectedPassValidity8, actualPassValidity8)

if __name__ == '__main__':
    unittest.main()
