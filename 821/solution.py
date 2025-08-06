from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        l, old = 0, s.index(c)
        new = old
        ans = [0] * n
        while l < n:
            ans[l] = min(abs(old-l), abs(new-l))
            l += 1
            if l > new:
                old = new
                i = new + 1
                while i < n:
                    if s[i] == c:
                        new = i
                        break
                    i += 1
        return ans


            



if __name__ == "__main__":
    s = "loveleetcode"
    c = "e"
    sol = Solution()
    print(sol.shortestToChar(s, c))
