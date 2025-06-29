from typing import List

class Solution:
    def sortSentence(self, s: str) -> str:
        d = {}
        for word in s.:
            key = word[:-1]
            val = word[-1]
            d[key] = val
        return ' '.join(list(dict(sorted(d.items(), key=lambda item: item[1]))))

def test_1():
    s = 
    
    sol = Solution()
    sol.sortSentence(s)
