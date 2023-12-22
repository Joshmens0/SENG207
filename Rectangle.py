from math import sqrt , pow
class Rectangle:
    #lets create a constructor method that stores the attribute for lenght and width
    def __init__(self,length,width):
        self.length=int(length)
        self.width=int(width)
    #lets create the Area of the plot
    #Note that the attribute of the width and lenght are placed into self     
    def Area(self):
        area=self.width*self.length
        print(area)
    #lets create the perimeter of the land
    def Perimeter(self):
        perimeter=2*(self.width + self.length)
        print(perimeter)
    #lets create the diagonal lenght of the land
    #Note that pow and sqrt is imported from the math library (from math import sqrt, pow)
    def diagonalLength(self):
        LenghtPow=pow(self.length,2)
        WidthPow=pow(self.width,2)
        LenghtSqrt=sqrt(LenghtPow)
        WidthSqrt=sqrt(WidthPow)
        Lenght=LenghtSqrt + WidthSqrt
        print(Lenght)
    
PlotOfLand=Rectangle(40,30)
PlotOfLand.Area()
PlotOfLand.Perimeter()
PlotOfLand.diagonalLength()