from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        ord = sorted(nums)

        n = len(nums)
        for i in range(n):
            ans.append(ord.index(nums[i]))
        return ans


def test_1():
    nums = [8,1,2,2,3]
    output = [4,0,1,1,3]
    sol = Solution()
    res = sol.smallerNumbersThanCurrent(nums)
    assert res == output
