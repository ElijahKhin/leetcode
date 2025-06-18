from typing import List

class Solution:
    def InsertionSort(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            j = i - 1
            val = nums[i]
            while j >= 0 and nums[j] > val:
                nums[j], nums[j+1] = val, nums[j]
                j -= 1

    def maximumProduct(self, nums: List[int]) -> int:
        self.InsertionSort(nums)
        val1 = nums[-1] * nums[-2] * nums[-3] 
        val2 = nums[0] * nums[1] * nums[-1]
        if val1 >= val2:
            return val1 
        else:
            return val2
    
def test_1():
    nums = [1, 3, 0, -1, -2, -5, 9]
    output = sorted(nums)
    sol = Solution()
    sol.InsertionSort(nums)
    print(nums)
    assert nums == output 

def test_2():
    nums = [1,2,3]
    sol = Solution()
    output = 6
    res = sol.maximumProduct(nums)
    assert res == output 

def test_3():
    nums = [1,2,3,4]
    sol = Solution()
    output = 24
    res = sol.maximumProduct(nums)
    assert res == output 

def test_4():
    nums = [-1,-2,-3]
    sol = Solution()
    output = -6
    res = sol.maximumProduct(nums)
    assert res == output 
