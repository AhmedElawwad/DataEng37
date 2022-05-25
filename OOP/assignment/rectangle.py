# Please create the following:
#
# - A rectangle class
# - It should have a width and a height
# - Give it the methods: get_area() and get_perimeter()
# - Give it appropriate str and repr representations
#
# - A square class
# - It should have a length
# - It needs get_area() and get_perimeter() and appropriate str and repr representations


class Rectangle:

    def __init__(self):
        self.height = 2.5
        self.width = 2.5

    def __repr__(self):
        return f" Rectangle size is with length={self.height} and width={self.width} "

    def __str__(self):
        return f" Rectangle size{self.height}, {self.width}"

    def set_height(self, rec_len=2.5):
        self.height = rec_len

    def set_width(self, rec_wid=2.5):
        self.width = rec_wid

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_area(self):
        return self.get_width() * self.get_height()

    def get_perimeter(self):
        return 2 * (self.get_width() + self.get_height())


if __name__ == '__main__':
    rect_1 = Rectangle()

    rect_1.set_height(4.0)
    rect_1.set_width(2.0)
    print("The area is   ", rect_1.get_area())
    print("The perimeter is  ", rect_1.get_perimeter())
    print(rect_1)
