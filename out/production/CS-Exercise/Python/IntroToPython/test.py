class point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x},{self.y}"

    def __mul__(self, other):
        return self.x*other.x


if __name__ == '__main__':
    x = point(5, 6)
    print(5 * x)
