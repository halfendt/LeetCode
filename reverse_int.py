class Solution:
    """
    7. Reverse Integer
    https://leetcode.com/problems/reverse-integer/
    """
    def reverse(self, x: int) -> int:
        num = int(str(abs(x))[::-1])
        if x >= 1:
            return 0 if num >= (2**31) or num <= -2**31 else num
        else:
            return 0 if num >= (2**31) or num <= -2**31 else -num