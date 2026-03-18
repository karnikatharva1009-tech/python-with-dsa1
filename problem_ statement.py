def security_key(number):
    visible=set()
    repeatednumber=0
    for ch in str(number):
        if ch in visible:
            repeatednumber+=1
        else:
           visible.add(ch)
    return repeatednumber if repeatednumber>0 else -1 
number=int(input("enter any number"))
print(security_key(number))            