# def addition(a,b):
#     return a+b
# print("Addition=",addition(50,60))

def Linear_Search(list,target):
    for i in range(len(list)):
        if list[i]==target:
            return i
    return -1
list=[10,20,30,40,50,60]
target=int(input("enter any number"))
index=Linear_Search(list,target)
print("Element found at index",index)
      