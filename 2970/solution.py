from typing import List

class Solution:
    def isIncr(self, nums):
        n = len(nums)
        for i in range(n-1):
            if nums[i] >= nums[i+1]:
                return False
        return True

    def isDecr(self, nums):
        n = len(nums)
        for i in range(n-1):
            if nums[i] <= nums[i+1]:
                return False
        return True

    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for l in range(n):
            for r in range(l, n):
                subarr = nums[:l] + nums[r+1:]
                if self.isIncr(subarr):
                    cnt += 1
        return cnt


if __name__ == "__main__":
    nums = [1,2,3,4]
    sol = Solution()
    output = 10
    res = sol.incremovableSubarrayCount(nums)
    print(res)
    print(res == output)
