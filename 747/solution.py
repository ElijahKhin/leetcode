from typing import List

class Solution:
    def BubbleSort(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            swp = False
            for j in range(len(nums) - i - 1):
                if nums[j] >= nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swp = True
            if swp == False:
                break

    def dominantIndex(self, nums: List[int]) -> int:
        maxx = max(nums)
        idx = next(i for i in range(len(nums)) if nums[i] == maxx)

        nums.sort()
        if nums[-2] > 0 and nums[-1] // nums[-2] >= 2:
            return idx
        else:
            if nums[-2] == 0 and maxx > 0:
                return idx
            return -1

def test_1():
    nums = [3,6,1,0]
    output = 1

    sol = Solution()
    res = sol.dominantIndex(nums)

    assert res == output 

def test_2():
    nums = [1,2,3,4]
    output = -1

    sol = Solution()
    res = sol.dominantIndex(nums)

    assert res == output 
