from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 1
        r = len(nums)
        while l<r:
            m = l+(r-l)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r=m
        return -1

          
if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 2 
    output = -1 
    sol = Solution()
    print(sol.search(nums, target) == output)
