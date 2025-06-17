from typing import List

class Solution:
    def Merge(self, nums, l, m, r):
        nl = m - l 
        nr = r - m

        lhs = [0] * nl
        rhs = [0] * nr

        for i in range(nl):
            lhs[i] = nums[i+l]
        for i in range(nr):
            rhs[i] = nums[i+m]
        i = 0
        j = 0
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
            k += 1
            i += 1

        while j < nr:
            nums[k] = rhs[j]
            k += 1
            j += 1

    def MergeSort(self, nums, l,r):
        if r - l > 1:
            m = l + (r-l) // 2
            self.MergeSort(nums, l, m)
            self.MergeSort(nums, m, r)
            self.Merge(nums, l, m, r)

    def missingNumber(self, nums: List[int]):
        self.MergeSort(nums, 0, len(nums))
        print(nums)
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

if __name__ == "__main__":
    nums = [3,0,1]
    sol = Solution()
    print(sol.missingNumber(nums))
