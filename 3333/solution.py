class Solution:
    def getNumberOfElements(self, word) -> int:
        cnt = 0
        for i in range(len(word) - 1):
            if word[i] != word[i+1]:
                cnt += 1
        return cnt + 1

    def getTupleKey(self, start: int, length: int) -> tuple:
        return tuple(range(start, start+length))

    def possibleStringCount(self, word: str, k: int) -> int:
        # All elements must be in result word -> Each substring has to be checked.
        # If k == len(word): return 1
        # Possible substrings must be unique. Note: should I use tuples of indices as keys in dict to track if substring already was count?

        n = len(word) 
        if k == n:
            return 1

        ttlEl = self.getNumberOfElements(word)
        key = self.getTupleKey(0, n)
        d[key] = 1

        
        for win in range(k, n - 1):
            start = 0
            loops = n - win + 1
            while loops >= 0:
                loops -= 1
                sub = word[start : start+win]
                el = self.getNumberOfElements(sub)
                if ttlEl == el:
                    key = self.getTupleKey(start, len(sum))
                



def main():
    word = "aabbccdd"
    k = 7
    sol = Solution()
    res = sol.possibleStringCount(word, k)
    print(res)

if __name__ == "__main__":
    main()
