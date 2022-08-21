class Circle:
    PI = 3.14

    def __init__(self, radius=1.0):
        self.radius = radius
        self.color = None

    def __str__(self):
        return f"r = {self.radius} c = {self.get_circumference()} a = {self.get_area()}"

    def get_area(self):
        return self.radius ** 2 * Circle.PI

    def get_circumference(self):
        return self.radius * 2 * self.PI

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color



circle1 = Circle(3)
circle2 = Circle()

circle1.set_color("Yellow")
circle2.set_color("Red")

circle1.get_color()
circle2.get_color()

print(circle1)
print(circle2)

print(f"Circle 1 radius is {circle1.radius} and its area is {circle1.get_area()}")
print(f"Circle 2 radius is {circle2.radius} and its area is {circle2.get_area()}")

print(f"Circle 1 circumference is {circle1.get_circumference()}")
print(f"Circle 2 circumference is {circle2.get_circumference()}")