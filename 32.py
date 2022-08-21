class Triangle():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        tri = """
*
**
***
****
        """
        values = f"The lenghts os the sides are {self.a},{self.b},{self.c}"
        sentence = f"The area is {self.find_area()} and the perimeter is {self.find_perimeter()}."
        return sentence + tri + values

    def find_area(self):

        s = self.find_perimeter() / 2
        area = abs((s * (s - self.a) * (s - self.b) * (s - self.c))) ** 0.5
        return area

    def find_perimeter(self):
        return self.a + self.b + self.c


    def print_triangle_type(self):
        if self.a == self.b == self.c:
            print("Equilateral Triangle")
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")


how_many = int(input("please enter how many triangles: "))
triangles = []
print(f"Now I'll ask for the lenght of the {how_many} triangles.")

for i in range(1, how_many + 1):
    # ternery operator
    a, b, c = [int(x) for x in input("please enter three lengths for triangle {i} like (1,2,3): ").split(',')]

    triangles.append(Triangle(a, b, c))

for triangle in triangles:
    print(triangle)