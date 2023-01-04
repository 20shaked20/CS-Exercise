'''
Python variables are created on the fly, meaning you can assign everything you want to a variable and the
interpreter will understand it.
'''

if __name__ == '__main__':
    a = 2
    print(type(a))  # int

    b = (1, 2, 3)
    print(type(b))  # tuple

    c = "Hello guys"
    print(type(c))  # str

    print(type(2.0))  # float

    print(True + 1)  # print 2!
