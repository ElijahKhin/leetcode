from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) > 2:
            return nums[-3]
        else:
            return nums[-1]

if __name__ == "__main__":
    nums = [-1,2,3]
    sol = Solution()
    print(sol.thirdMax(nums))
