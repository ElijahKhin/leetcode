from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n+1)
        for i in range(1, n+1):
            prefix[i] = nums[i-1] + prefix[i-1]
        for i in range(n):
            if prefix[i] == prefix[-1] - prefix[i+1]:
                return i
        return -1
 
if __name__ == "__main__":
    nums = [2,1,-1]
    sol = Solution()
    print(sol.pivotIndex(nums))
