class Solution:
    """
    14. Longest Common Prefix
    https://leetcode.com/problems/longest-common-prefix/
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return ''.join(prefix)