from typing import List

class Solution:
    def getPrefix(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        for i in range(1, n):
            prefix[i] = nums[i-1] + prefix[i-1]
        return prefix



    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = self.getPrefix(nums) 
        nums.reverse()
        right = self.getPrefix(nums) 
        right.reverse()
        return [abs(first - second) for first, second in zip(left, right)]

if __name__ == "__main__":
    nums = [10,4,8,3]
    sol = Solution() 
    print(sol.leftRightDifference(nums))
