class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = r = i = 0
        cnt = 0
        res = 0
        while r <= n and i < n:
            ch = s[i]
            print("ch:", s[i])
            i += 1
            print("array: ", s[l : r])
            if ch not in s[l : r]:
                r += 1
            else:
                while s[l] != ch:
                    l += 1
                l += 1
                r += 1
                if l == r:
                    r += 1
            print("r: ", r)
            if len(s[l : r]) > res:
                res = len(s[l : r])
        return res

if __name__ == "__main__":
    s = "pwwkew"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))

