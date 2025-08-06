class Solution:
    def circle(self, s, l, r, flg):
        while l < r:
            if s[l] != s[r]:
                if r - l == 1:
                    if flg:
                        return True
                    else:
                        return False
                if flg:
                    flg = False
                    left = self.circle(s, l+1, r, flg)
                    right = self.circle(s, l, r-1, flg)
                    if left or right:
                        return True
                    else:
                        return False
                else:
                    return False
            l += 1
            r -= 1
        return True


    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 
        if self.circle(s, l, r, True):
            return True
        else:
            return False




if __name__ == "__main__":
    s = "abc"
    sol = Solution()
    print(sol.validPalindrome(s))
