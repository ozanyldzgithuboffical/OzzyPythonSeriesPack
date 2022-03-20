# @Author: Ozan YILDIZ@2022
# any returns true if any of the elements is iterable otherwise returns false
# Integer,double, float such objects are not iterable but set,list,tuple,string are.
bridges = ['Mehmet', 'Selim', 'Canakkale', 'Istanbul']
bridgeCount = 4
if __name__ == '__main__':
    # any true case
    print("Bridges any:", any(bridges))
    # any operator
    try:
        print("Bridge any:", any(bridgeCount))
    except:
        print("Integer object is not iterable")
