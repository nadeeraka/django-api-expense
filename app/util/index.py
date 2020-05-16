import sys

def getLowerstVal(array):
    if array not in locals():
        return -1
    val = array[0]
    for i in array:
        if i < val:
            val = i
        return i

#get all count
def getCount(array):
    if array not in locals():
        return -1
    count = 0
    for i in array:
        count +=i
    return count


#get avarage
def getAva(array):
    if array not in locals():
        return -1
    if getCount(array)>0:
        return getCount(array)/len(array)


