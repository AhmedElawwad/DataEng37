


class Square:

    def __init__(self):
        self.length = 3
        self.sides = 4

    def __repr__(self):
        return f" Rectangle size is with length={self.length}"

    def __str__(self):
        return f" Square length ={self.length}"

    def set_length(self, sqr_len=2.5):
        self.length = sqr_len

    def set_sides(self, rec_sides=4):
        self.sides = rec_sides

    def get_area(self):
        return pow(self.sides, 2)

    def get_perimeter(self):
        return 4 * self.get_area()


if __name__ == '__main__':
    seq_1 = Square()

    seq_1.set_length(2)

    print("The area ", seq_1.get_area())
    print("The perimeter ", seq_1.get_perimeter())
    print(seq_1)
