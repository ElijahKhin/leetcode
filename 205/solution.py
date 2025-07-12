class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        d = {}
        for i in range(n):
            if d.get(s[i], 0) == 0:
                if t[i] not in d.values():
                    d[s[i]] = t[i]
                else:
                    return False
            else:
                if d[s[i]] != t[i]:
                    return False
        return True

if __name__ == "__main__":
    t = "badc"
    s = "baba" 
    sol = Solution()
    res = sol.isIsomorphic(s, t)
    print(res)
                
