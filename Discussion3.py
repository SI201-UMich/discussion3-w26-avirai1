import math

class Rectangle():
    # Create the constructor "__init__" method

    def __init__(self, length, width):
        self.length = length
        self.width = width



    # Create the "__str__" method

    def __str__(self):
        return str(self.length) + ", " + str(self.width)



    # Create the "area_calculator" method

    def area_calculator(self):
        return self.length * self.width


    # Create the "__eq__" method
    # 
    # Returns a boolean value

    def __eq__(self, value):
        return self.length == value.length and self.width == value.width


    


def main():
    r1 = Rectangle(10, 10)
    # call the __str__ method
    print(r1)
    # call the area_calculator method
    print("Area:", r1.area_calculator())


    r2 = Rectangle(10, 15)
    print(r2)
    print("Area:", r2.area_calculator())
    # call the __eq__ method
    print(r1 == r2)
    print()

if __name__ == "__main__":
    main()