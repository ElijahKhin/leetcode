from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        lr = sorted(list(set(nums)))
        nums.sort()
        if len(lr) == 1:
            return 0
        vals = []
        for i in range(1, len(lr)):
            cnt = 0
            for j in range(len(nums)):
                if nums[j] >= lr[i - 1] and nums[j] <= lr[i]:
                    cnt += 1
            vals.append(cnt)
        return max(vals)

def test_1():
    sol = Solution()
    nums = [1,2,2,1]
    output = 4
    assert sol.findLHS(nums) == output

