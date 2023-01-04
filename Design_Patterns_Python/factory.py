from __future__ import annotations
from abc import ABC, abstractmethod

"""
The Factory design pattern is a creational design pattern that enables you to create objects in a base class.
it allows the children classes to override the object creation method and alter the type of objects created.
"""


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()

        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


class ConcreteCreator1(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "CP1"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "CP2"


def client(creator: Creator) -> None:
    print(creator.some_operation())


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client(ConcreteCreator1())

    print("App: Launched with the ConcreteCreator2.")
    client(ConcreteCreator2())
