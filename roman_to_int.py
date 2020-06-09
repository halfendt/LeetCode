class Solution:
    """
    13. Roman to Integer
    https://leetcode.com/problems/roman-to-integer/
    """
    def romanToInt(self, s: str) -> int:
        sym_val = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 
                   50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        if not s:
            return 0
        for value, sym in sym_val.items():
            if s.startswith(sym):
                return value + Solution.romanToInt(self, s[len(sym):])