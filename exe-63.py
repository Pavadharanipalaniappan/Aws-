import math
class Shape:
    def __init__(self, side):
        self.side = side

    def area(self):
        pass

    def perimeter(self):
        pass
class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        super().__init__(side1)
        self.base = base
        self.height = height
        self.side2 = side2
        self.side3 = side3
    def area(self):
        return 0.5 * self.base * self.height
    def perimeter(self):
        return self.side + self.side2 + self.side3
class Rhombus(Shape):
    def __init__(self, diagonal1, diagonal2, side):
        super().__init__(side)
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
    def area(self):
        return 0.5 * self.diagonal1 * self.diagonal2
    def perimeter(self):
        return 4 * self.side
class Pentagon(Shape):
    def area(self):
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * self.side ** 2

    def perimeter(self):
        return 5 * self.side

class Hexagon(Shape):
    def area(self):
        return 1.5 * math.sqrt(3) * self.side ** 2

    def perimeter(self):
        return 6 * self.side

# Example usage
shape_type = input("Enter shape type (triangle, rhombus, pentagon, hexagon): ")
if shape_type == "triangle":
    base = float(input("Enter base length: "))
    height = float(input("Enter height: "))
    side1 = float(input("Enter side 1 length: "))
    side2 = float(input("Enter side 2 length: "))
    side3 = float(input("Enter side 3 length: "))
    shape = Triangle(base, height, side1, side2, side3)
elif shape_type == "rhombus":
    diagonal1 = float(input("Enter diagonal 1 length: "))
    diagonal2 = float(input("Enter diagonal 2 length: "))
    side = float(input("Enter side length: "))
    shape = Rhombus(diagonal1, diagonal2, side)
elif shape_type == "pentagon":
    side = float(input("Enter side length: "))
    shape = Pentagon(side)
elif shape_type == "hexagon":
    side = float(input("Enter side length: "))
    shape = Hexagon(side)
else:
    print("Invalid shape type")

if shape_type in ["triangle", "rhombus", "pentagon", "hexagon"]:
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
