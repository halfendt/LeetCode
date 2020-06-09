from collections import Counter 

class Solution:
    """
    438. Find All Anagrams in a String
    https://leetcode.com/problems/find-all-anagrams-in-a-string/
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pC = Counter(p)
        res = []
        window = None
        for i in range(len(s)-len(p)+1):
            if i==0: 
                window = Counter(s[i:i+len(p)])
            else:
                window -= {s[i-1]:1}
                window += {s[i+len(p)-1]:1}
            if pC == window: 
                res.append(i)
        return res