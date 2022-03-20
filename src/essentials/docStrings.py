import math


# @Author: Ozan YILDIZ@2022
# Doc strings are used to express a logic/information about the code block
def cylinder(radius, height):
    """Function to return volume of Cylinder """
    return math.pi * math.pow(radius, 2) * height


print(cylinder.__doc__)

if __name__ == '__main__':
    cylinderVolume = cylinder(2, 3)
    print("Cylinder Volume is:", cylinderVolume)
