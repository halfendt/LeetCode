class Solution:
    """
    1446. Consecutive Characters
    https://leetcode.com/problems/consecutive-characters/
    """
    from itertools import groupby
    def maxPower(self, s: str) -> int:
        return max(sum(1 for _ in group) for _, group in groupby(s))

