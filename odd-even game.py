n=int(input("enter the size of list"))
thislist=[]
listeven=[]
listodd=[]
for i in range(n):
    a=int(input("enter the number"))
    thislist.append(a)
print(thislist)
for x in thislist:
    if x%2==0:
        listeven.append(x)
    else:
        listodd.append(x)    
print(listeven)
print(listodd)              
