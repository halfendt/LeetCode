class Solution:
    """
    28. Implement strStr()
    https://leetcode.com/problems/implement-strstr/
    """
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '': return 0
        try:
            return haystack.index(needle)
        except:
            return -1