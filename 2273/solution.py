from typing import List
from collections import Counter

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        i = 1
        while i < len(words):
            print(words[i-1], words[i])
            if Counter(words[i]) == Counter(words[i-1]):
                del words[i]
            else:
                i += 1
        return words



if __name__ == "__main__":
    words = ["abba","baba","bbaa","cd","cd"]
    output = ["abba","cd"]
    sol = Solution()
    res = sol.removeAnagrams(words)
    print(res)
    print(res == output)
