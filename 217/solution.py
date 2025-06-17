from typing import List

class Solution:
    def insertionSort(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            j = i - 1
            val = nums[i]
            while nums[j] < val and j >= 0:
                nums[j], nums[j+1] = val, nums[j]
                j -= 1
                
        print(nums)
        return nums

    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = self.insertionSort(nums)
        print(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True;
        return False

nums = [1,2,3,1]
sol = Solution();

res = sol.containsDuplicate(nums)
print(res)
