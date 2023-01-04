"""
The Singleton design pattern is one of the simplest yet highly beneficial creation design patterns.
This pattern ensures that only one instance of a kind exists.
Whenever some client code asks for an instance of a class, the same instance is returned every time.
"""


class FooMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Foo(metaclass=FooMeta):
    def some_func_here(self):
        return 42


if __name__ == "__main__":

    foo1 = Foo()
    foo2 = Foo()

    if id(foo1) == id(foo2):
        print("Both variables refer to the same object")
    else:
        print("Both variables refer to different objects")
