

# operation on list
# Append function

list=[1,2,3,4,5]
list.append(10)
print(list)

# insert function
list.insert(1,20)
print(list)

# list reverse
list=[1,2,3,4,5]
list.reverse()
print(list)

# list indexing
print(list.index(3))

# list count
list=[1,2,3,4,4,4,4,5]
print("count of 4 =",list.count(4))

# list sort
list2=[6,4,8,6,2,1,4,9,11,5]
print(list2)
list2.sort()
print(list2)

# remove duplicate
num=[1,2,3,1,1,2,2,3,4,4]
data=[]
for i in num:
    if i not in data:
        data.append(i)
print("Actual list =",num)
print("After removing dulicate:",data)