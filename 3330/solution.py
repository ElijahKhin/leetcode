class Solution:
    def possibleStringCount(self, word: str) -> int:
        # form list that represents 'word' like 431 for word = aaaabbbc
        prev = word[0]
        n = len(word)
        cnt = 1
        lst = []
        for i in range(1, n):
            if word[i] == prev:
                cnt += 1
            else:
                lst.append(cnt)
                cnt = 1
                prev = word[i]
        lst.append(cnt)
        print(lst)
        res = 0
        for i in lst:
            res += i - 1
        return res + 1

if __name__ == "__main__":
    word = "abbcccc"
    sol = Solution()
    sol.possibleStringCount(word)
