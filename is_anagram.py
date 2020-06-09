class Solution:
    """
    242. Valid Anagram
    https://leetcode.com/problems/valid-anagram/
    """
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)