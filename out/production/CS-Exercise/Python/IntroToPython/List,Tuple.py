if __name__ == '__main__':
    # list is mutable whilst tuple is immutable

    lst = ["5", 6, True, "False"]
    lst3 = ["Hello", "Str", "bla", "Yoni"]
    lst2 = [6, 7, 8, 11, 2, 3, 1]
    print(lst[0])

    tpl = ("5", 6, True)
    print(tpl[0])

    for element in lst:
        print(element, end=" ")

    print("")
    print(tpl[1:])  # like we studied from strings, here we can print from certain point to end by doing this

    # list methods #
    # print(dir(lst))
    # lst[1] = 7
    lst.append(5)
    dic = {"Hello": 2,
           "Bla": 3}
    lst3.sort()
    print(lst3)
