from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = sum(arr)
        n = len(arr)
        prefix = [0] * (n+1) 
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + arr[i-1]
        right = 3
        while right <= n:
            for left in range(n-right+1):
                res += prefix[right+ left] - prefix[left]
            right += 2
        return res



        
if __name__ == "__main__":
    arr = [10,11,12]
    sol = Solution()
    print(sol.sumOddLengthSubarrays(arr))
