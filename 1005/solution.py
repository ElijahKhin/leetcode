from typing import List

class Solution:
    def BubbleSort(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            swp = False
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swp = True
            if swp == False:
                break

                
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        minn = min(nums)
        if minn >= 0:
            if k % 2 == 0:
                return sum(nums)
            else:
                return sum(nums) - 2* min(nums)
        else:
            self.BubbleSort(nums)
            i = 0
            while nums[i] < 0 and k > 0 and i < len(nums):
                nums[i] = -nums[i]
                k -= 1
                i += 1
            print(nums)
            if k > 0:
                if k % 2 == 0:
                    return sum(nums)
                else:
                    return sum(nums) - 2*min(nums)
            return sum(nums)


def test_1():
    nums = [4,2,3]
    k = 1 
    output = 5 
    sol = Solution()
    res = sol.largestSumAfterKNegations(nums, k)
    assert res == output

def test_2():
    nums = [3,-1,0,2]
    k = 3 
    output = 6 
    sol = Solution()
    res = sol.largestSumAfterKNegations(nums, k)
    assert res == output

def test_3():
    nums = [2,-3,-1,5,-4]
    k = 2 
    output = 13
    sol = Solution()
    res = sol.largestSumAfterKNegations(nums, k)
    assert res == output
