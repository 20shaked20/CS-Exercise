if __name__ == '__main__':

    x = 0
    while x < 5:
        print(x)
        # ++x or x++ does not work in python!
        x += 1

    for i in [0, 1, 2]:
        print(i * i, end=" ")  # print in the same line! nice to know

    print(" ")
    for i in range(0, 5, 2):
        print(i, end=" ")

