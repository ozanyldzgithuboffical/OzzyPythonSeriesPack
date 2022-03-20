# @Author: Ozan YILDIZ@2022
# Tuple is an unordered sequence of items as a list, and it is enclosed with ()
# Tuples are immutable so once they are created they can not be changed.

myTuple = ("Hello", 2, u"\u0048")
if __name__ == '__main__':
    print("Tuple[0]", myTuple[0])
    print("Tuple[1]", myTuple[1])
    print("Tuple[2]", myTuple[2])
    # generate error
    try:
        myTuple[2] = "World"
    except:
        print("Tuple value can not be changed, they are immutable")
