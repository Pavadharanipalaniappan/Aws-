import math
class Shape:
    def area(self, *args):
        pass
    def perimeter(self, *args):
        pass

class Triangle(Shape):
    def area(self, base, height):
        return 0.5 * base * height
    def perimeter(self, side1, side2, side3):
        return side1 + side2 + side3

class Rhombus(Shape):
    def area(self, diagonal1, diagonal2):
        return 0.5 * diagonal1 * diagonal2
    def perimeter(self, side):
        return 4 * side

class Pentagon(Shape):
    def area(self, side):
        return 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side ** 2
    def perimeter(self, side):
        return 5 * side

class Hexagon(Shape):
    def area(self, side):
        return (3 * math.sqrt(3) * side ** 2) / 2
    def perimeter(self, side):
        return 6 * side
       
triangle = Triangle()
triangle_area = triangle.area(8, 5)
triangle_perimeter = triangle.perimeter(5, 7, 10)
print("Triangle \n Area: ",(triangle_area),"Perimeter: ",(triangle_perimeter))

rhombus = Rhombus()
rhombus_area = rhombus.area(10, 12)
rhombus_perimeter = rhombus.perimeter(8)
print("Rhombus \n Area: ",(rhombus_area)," Perimeter: ",(rhombus_perimeter))

pentagon = Pentagon()
pentagon_area = pentagon.area(7)
pentagon_perimeter = pentagon.perimeter(5)
print("Pentagon \n Area: ",(pentagon_area)," Perimeter: ",(pentagon_perimeter))
hexagon = Hexagon()
hexagon_area = hexagon.area(6)
hexagon_perimeter = hexagon.perimeter(8)
print("Hexagon \n Area: ",(hexagon_area), "Perimeter: ",(hexagon_perimeter))