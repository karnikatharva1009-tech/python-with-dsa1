
def Linear_Search(list,target):
    i=0
    while i<len(list):
        if list[i]==target:
            return i
    i+=1    
    return -1
list=[10,20,30,40,50,60]
target=int(input("enter any number"))
index=Linear_Search(list,target)
print("Element found at index",index)

