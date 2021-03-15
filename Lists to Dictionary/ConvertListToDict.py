#!/usr/bin/env python

#Function to convert 2 lists to Dictionary
def ConvertListsToDict(keys, values):
    if (len(keys) == 0):
        return ("Empty keys")

    elif (len(values) >= len(keys)):
        dictionary = dict(zip(keys, values))
        return (dictionary)

    else:
        extraKeys = len(keys) - len(values)
        l = [None] * extraKeys
        values.extend(l)
        dictionary = dict(zip(keys, values))
        return (dictionary)

#main program
def main():
    list1 = ['a', 'b', 'c']
    list2 = [1, 5, 3, 4]
    Dict = ConvertListsToDict(list1, list2)
    print(Dict)


if __name__ == '__main__':
    main()
