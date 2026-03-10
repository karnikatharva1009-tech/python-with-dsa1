# find the largest number
a,b,c=10,20,30
if a>=b and a>=c:
    print("a is greater")
if b>=a and b>=c:
    print("b is greater")
if c>=a and c>=b:
    print("c is greater")
print(max(a,b,c))            