if __name__ == '__main__':
    greet = "hello"
    age = "20"

    # print formats #
    print(greet + " My age: " + age)

    print("{} My Age: {}".format(greet, age))

    print(f"{greet} My Age: {age}")

    # slicing #
    print(greet[-1])
    print(greet[0])
    print(greet[0:3])
    print(greet[0:-1])

    # methods #
    print(greet.upper())
    print(len(greet))
    print(greet.find("o"))  # shows where it is in location
    print(dir(greet))  # shows all the available methods to use on this object.
