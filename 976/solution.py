from typing import List

class Solution:
    def insertionSort(self, nums) -> None:
        for i in range(1, len(nums)):
            j = i - 1
            val = nums[i]
            while j >= 0 and nums[j] < val:
                nums[j], nums[j+1] = val, nums[j]
                j -= 1

    def largestPerimeter(self, nums: List[int]) -> int:
        self.insertionSort(nums)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2] 
        return 0


def test_1():
    nums = [2,1,2]
    output = 5 
    
    sol = Solution()
    res = sol.largestPerimeter(nums)

    assert res == output 

def test_2():
    nums = [1,2,1,10] 
    output = 0 
    
    sol = Solution()
    res = sol.largestPerimeter(nums)

    assert res == output 

if __name__ == "__main__":
    sol = Solution()

    nums = [2,2,1]
    sol.InsertionSort(nums)
    print(nums)
