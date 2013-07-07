# http://en.wikibooks.org/wiki/Computer_Science_Design_Patterns/Bridge_Pattern#Python


# ConcreteImplementor 1/2
class DrawingAPI1:
    def drawCircle(self, x, y, radius):
        print('API1.circle at {}:{} radius {}'.format(x, y, radius))


# ConcreteImplementor 2/2
class DrawingAPI2:
    def drawCircle(self, x, y, radius):
        print('API2.circle at {}:{} radius {}'.format(x, y, radius))


# Refined Abstraction
class CircleShape:
    def __init__(self, x, y, radius, drawingAPI):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__drawingAPI = drawingAPI
 
    # low-level i.e. Implementation specific
    def draw(self):
        self.__drawingAPI.drawCircle(self.__x, self.__y, self.__radius)
 
    # high-level i.e. Abstraction specific
    def resizeByPercentage(self, pct):
        self.__radius *= pct


def main():
    shapes = (
        CircleShape(1, 2, 3, DrawingAPI1()),
        CircleShape(5, 7, 11, DrawingAPI2())
    )
 
    for shape in shapes:
        shape.resizeByPercentage(2.5)
        shape.draw()
 

if __name__ == "__main__":
    main()
