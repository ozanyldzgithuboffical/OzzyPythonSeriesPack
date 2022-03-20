# @Author: Ozan YILDIZ@2022
def outerFunc():
    # local val
    val = 10

    def innerFunc():
        # global val overriden
        global val
        val = 12
        print("Nested-Inner Local Val:", val)

    innerFunc()
    print("Local Val:", val)


# most-global val
val = 15
if __name__ == '__main__':
    outerFunc()
print("Global Val:", val)
