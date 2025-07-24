class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        rev_num = 0
        while num > 0:
            digit = num % 10
            rev_num = rev_num * 10 + digit
            num //= 10
        return x == rev_num
    
print(Solution().isPalindrome(121))
