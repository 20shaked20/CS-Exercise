"""
Simple Magics methods we can use in python.
This is one of the good things we should consider when using python!
"""

"""
In this example i'll show you how we can create our own string method.

https://www.tutorialsteacher.com/python/magic-methods-in-python -> more to see :)

"""


class Magics:

    # magic method to initiate object
    def __init__(self, string: str, num: int):
        self.string = string
        self.num = num

    # repr -> print our string object
    # def __repr__(self):
    #     return 'Object: {}'.format(self.string)

    def __str__(self):
        return f'The String is: {self.string}\n' \
               f'The number is: {self.num}'

    def add(self, other: str):
        self.string += other

    def add_return(self, other: str) -> str:
        return self.string + other

    # add -> combines on or more
    def __add__(self, other: str) -> str:  # +++++++++
        return self.string + other

    # ge -> greater equal >=
    def __ge__(self, other: int):
        return self.num > other if True else False  # explain -> return true if num > other else, false.


# Driver Code
if __name__ == '__main__':
    # object creation
    m_m1 = Magics('Hey', 10)
    m_m2 = Magics("Sup", 5)

    # concatenate String object and a string
    print(m_m1 + " You, " + "How are you doing?")
    print(m_m1.add_return(" You") + m_m1.add_return(" How are you doing?"))

    # here it prints only the object type and not the __str__//__repr__ why?, because it recognizes as the normal object
    # it will invoke either repr or str, according to its placement ( the last one read ).
    print(m_m1)
    print(m_m1 >= 5)
