class Solution:
    """
    9. Palindrome Number
    https://leetcode.com/problems/palindrome-number/
    """
    def isPalindrome(self, x: int) -> bool:
        return False if x < 0 else str(x) == str(x)[::-1]