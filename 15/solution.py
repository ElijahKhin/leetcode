from typing import List

class Solution:
    def m(self, nums, l, m, r):
        nl = m - l
        nr = r - m

        lhs = [0] * nl
        rhs = [0] * nr

        for i in range(nl):
            lhs[i] = nums[l + i]
        for i in range(nr):
            rhs[i] = nums[m + i]

        i = j = 0
        k = l
        while i < nl and j < nr:
            if lhs[i] < rhs[j]:
                nums[k] = lhs[i]
                i += 1
            else:
                nums[k] = rhs[j]
                j += 1
            k += 1

        while i < nl:
            nums[k] = lhs[i]
            i += 1
            k += 1

        while j < nr:
            nums[k] = rhs[j]
            j += 1
            k += 1

    def ms(self, nums, l, r):
        if r - l > 1:
            m = l + (r - l) // 2
            self.ms(nums, l, m)
            self.ms(nums, m, r)
            self.m(nums, l, m, r)
        

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.ms(nums, 0, len(nums))
        res = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                ttl = nums[i] + nums[l] + nums[r]
                if ttl == 0:
                    res.append([nums[i], nums[l], nums[r]]) 
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif ttl < 0:
                    l += 1
                else:
                    r -= 1
        return res




if __name__ == "__main__":
    nums1 = [-1,0,1,2,-1,-4]
    nums2 = [0,1,1]
    nums3 = [0,0,0]
    sol = Solution()
    res = sol.threeSum(nums1)
    print(res)
    res = sol.threeSum(nums2)
    print(res)
    res = sol.threeSum(nums3)
    print(res)



