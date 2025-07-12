def guess(num: int) -> int:
    real_num = 1
    if num == real_num:
        return 0
    if num > real_num:
        return -1
    if num < real_num:
        return 1

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n + 1
        while l < r:
            m = l + (r-l) // 2
            res = guess(m)
            if res == 0:
                return m
            elif res == 1:
                l = m+1
            else:
                r = m
        return -1

if __name__ == "__main__":
    n = 2
    sol = Solution()
    print(sol.guessNumber(n))
