# @Author: Ozan YILDIZ@2022
# Eval parses the expression and execute to simulate the result
val1 = 12
val2 = 3
if __name__ == '__main__':
    # eval operation on dividing
    result = eval('val1 / val2')
    print("Result expected 4 and actual:", int(result))
