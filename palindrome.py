class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringdata=str(x)
        return stringdata==stringdata[::-1]