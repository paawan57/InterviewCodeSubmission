#!/usr/bin/env python

import re
import time

#Method to validate password using Regular Expressions
def matchPasswordWithRE(password):
    if (len(password) >= 1 and len(password) <= 20):

        passRegex = re.compile(r'^([a-zA-Z]+)([a-zA-Z0-9-.]*)([a-zA-Z0-9]+)|([a-zA-Z]+)([a-zA-Z0-9]*)$')
        passMatch = passRegex.fullmatch(password)

        if (passMatch != None):
            return ("Valid")
        else:
            return ("Invalid")
    else:
        return ("Invalid")

#Method to validate password without using Regular Expressions
def matchPasswordWithoutRE(password):
    if (len(password) >= 1 and len(password) <= 20):
        if (password[0].isalpha()):
            if (password[len(password) - 1].isalnum()):
                if (all(bool(char.isalnum()) | bool(char in ['.', '-']) for char in password)):
                    return ("Valid")
                else:
                    return ("Invalid")
            else:
                return ("Invalid")
        else:
            return ("Invalid")
    else:
        return ("Invalid")

#main method
def main():
    password = 'a6-.6ak-er---12'

    print("###Password Check Using Regular Expressions###")
    t1 = time.time()
    passwordValidity1 = matchPasswordWithRE(password)
    methodTiming1 = time.time() - t1
    print("Password is", passwordValidity1)
    print("Time taken by using RE :", methodTiming1)

    print("\n")

    print("###Password Check without Regular Expressions###")
    t2 = time.time()
    passwordValidity2 = matchPasswordWithoutRE(password)
    methodTiming2 = time.time() - t2
    print("Password is", passwordValidity2)
    print("Time taken without RE :", methodTiming2)


if __name__ == '__main__':
    main()
