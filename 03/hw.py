
class Shape:
    def __init__(self):
        pass
    def __repr__(self):
        return "Shape"

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    def getArea(self):
        return self.l * self.w
    def __repr__(self):
        return "Rectangle, area = %f" %self.getArea()

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        return 3.14 * (self.radius ** 2)
    def __repr__(self):
        return "Circle, area = %f" %self.getArea()

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h
    def getArea(self):
        return 0.5 * self.b * self.h
    def __repr__(self):
        return "Triangle, area = %f" %self.getArea()

        

totalShapes = []
try:
    file = open(r'D:\DevSource\Tamu\GeoInnovation\_GISProgramming\code\03\shapes.txt', 'r')
    lines = file.readlines()
    file.close()

    for line in lines:
        components = line.split(",")
        shape = components[0]

        if shape == 'Rectangle':
            x = int(components[1])
            y = int(components[2])
            totalShapes.append(Rectangle(x, y))
        elif shape == 'Circle':
            x = int(components[1])
            totalShapes.append(Circle(x))
        elif shape == 'Triangle':
            x = int(components[1])
            y = int(components[2])
            totalShapes.append(Triangle(x, y))
        else:
            pass
    
    for shape in totalShapes:
        print(shape.getArea())
    
except IOError:
    print("An error has occurred")