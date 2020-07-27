import sys

def getCount(array):
    if array not in locals():
        return -1
    count = 0
    for i in array:
        count +=i
    return count

sys.modules[__name__] = getCount