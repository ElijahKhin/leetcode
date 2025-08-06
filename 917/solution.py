class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n = len(s)
        l, r = 0, n - 1
        res = [0] * n
        while l <= r:
            if s[l].isalpha() and s[r].isalpha():
                res[l], res[r] = s[r], s[l]
                l += 1
                r -= 1

            elif s[r].isalpha() == False:
                res[r] = s[r]
                r -= 1
            elif s[l].isalpha() == False:
                res[l] = s[l]
                l += 1
            
        return ''.join(res)

if __name__ == "__main__":
    s = "Test1ng-Leet=code-Q!"
    sol = Solution()
    print(sol.reverseOnlyLetters(s))
