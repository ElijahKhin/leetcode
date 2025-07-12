from typing import List
from bisect import bisect_right, bisect_left

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        cnt_neg = bisect_left(nums, 0)
        cnt_pos = len(nums) - bisect_right(nums, 0)
        return cnt_neg if cnt_neg > cnt_pos else cnt_pos

if __name__ == "__main__":
    nums = [-2,-1,-1,1,2,3]
    output = 3
    sol = Solution()
    res = sol.maximumCount(nums)
    print(res)
    print(res == output)
