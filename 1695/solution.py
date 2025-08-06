from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        st = set(nums)

        if len(st) == 1: 
            return nums[0]

        if len(st) == n: 
            return sum(nums)

        max_size = 0
        l, r = 0, 1
        while r <= n:
            new_el = nums[r-1]
            print(new_el, nums[l:r-1])
            if new_el in nums[l:r-1]:
                l += nums[l:r].index(new_el) + 1
            print(nums[l:r])
            summ = sum(nums[l:r])
            if max_size < summ:
                print("yes")
                max_size = summ 
            r += 1

        return max_size




if __name__ == "__main__":
    nums = [4,2,4,5,6]
    output = 8
    sol = Solution()
    res = sol.maximumUniqueSubarray(nums)
    print(res)
    print(res == output)
        
