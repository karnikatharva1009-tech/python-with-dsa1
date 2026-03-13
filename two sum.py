def solveMeFirst(a,b):
    return (a+b)
	# Hint: Type return a+b below


num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)

#type 2
class Solution:
    def twoSum(self, nums, target):
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if(nums[i]+nums[j]==target):
                    return[i,j]