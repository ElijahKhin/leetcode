class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix = [0] * (n+1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + i
        for i in range(1,n):
            if prefix[-1] - prefix[i-1] == prefix[i]:
                return i
        return -1

if __name__ == "__main__":
    n = 8
    sol = Solution()
    print(sol.pivotInteger(n))

