def hello():
    print("Hello")


def print_request(msg1: str, msg2: str) -> None:
    print(f"{msg1}, {msg2} ")


def multiply(num1: int, num2: int) -> int:
    return num1 * num2


if __name__ == '__main__':
    hello()
    print_request("Hello", "Students")
    print_request(5, "Hello")
    print(5*(multiply(5, " Shaked ")))
