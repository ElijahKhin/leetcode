from typing import List

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        cty = 0
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1, n-1):
                if nums[i] == nums[j]: continue
                for k in range(j+1, n):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]: 
                        print(nums[i], nums[j], nums[k])
                        cty += 1
        return cty
        

if __name__ == "__main__":
    nums = [4,4,2,4,3]
    output = 3
    sol = Solution()
    res = sol.unequalTriplets(nums)
    print(res)
    print(res == output)
