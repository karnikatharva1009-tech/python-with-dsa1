# Find and print second largest 
number=[12,56,78,89,45,65,71]
maximum=second_largest=float("-inf")
for i in number:
    if i>maximum:
        second_largest=maximum
        maximum=i
    elif i>second_largest and i!=maximum:
         second_largest=i
print("second_largest value:",second_largest)          