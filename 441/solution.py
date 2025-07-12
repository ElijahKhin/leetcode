class Solution:
    def arrangeCoins(self, n: int) -> int:
        # invariant: Each iteration step is less or equal than reminder of n
        cnt = 0
        step = 1 
        while step <= n:
            cnt += 1
            n -= step
            step += 1
        return cnt

if __name__ == "__main__":
    n = 5
    sol = Solution()
    output = 2
    print(sol.arrangeCoins(n) == output)
