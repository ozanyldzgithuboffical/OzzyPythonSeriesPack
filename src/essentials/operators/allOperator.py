# @Author: Ozan YILDIZ@2022
# any returns true if any of the elements is iterable otherwise returns false
# Integer,double, float such objects are not iterable but set,list,tuple,string are.
bridges = ['Mehmet', 4, 'Canakkale', 'Istanbul']
bridgeCount = 4
if __name__ == '__main__':
    # all true case
    print("Bridges any:", all(bridges))
    # all false case
    try:
        print("Bridge any:", all(bridgeCount))
    except:
        print("Integer object is not iterable")
