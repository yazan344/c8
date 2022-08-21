class Square:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.color = None

    def __str__(self):
        return f"length = {self.length} width = {self.width}"

    def find_area(self):
        return self.length * self.width

    def find_perimeter(self):
        return 2 * self.length + 2 * self.width

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color



square_1 = Square(10, 20)
square_2 = Square(6, 4)

square_1.set_color("pink")
square_2.set_color("white")

print(square_1.get_color())
print(square_2.get_color())

print(square_1)
print(square_2)

print(f"the area of square 1 is :{square_1.find_area()}")
print(f"the area of square 2 is :{square_2.find_area()}")

print(square_1.length)
print(square_1.width)

print(square_2.length)
print(square_2.width)

print(f"the perimeter of square 1 is {square_1.find_perimeter()}")
print(f"the perimeter of square 2 is {square_2.find_perimeter()}")