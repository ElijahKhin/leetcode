from typing import List

class Solution:
    def Merge(self, nums, l, m, r):
        nl = m - l
        nr = r - m
        lhs = [0] * nl
        rhs = [0] * nr

        for i in range(nl):
            lhs[i] = nums[i + l]

        for i in range(nr):
            rhs[i] = nums[m + i]

        i = j = 0
        k = l
        while i < nl and j < nr:
            if lhs[i] <= rhs[j]:
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


    def MergeSort(self, nums, l, r):
        if r - l > 1:
            m = l + (r-l) // 2
            self.MergeSort(nums, l, m)
            self.MergeSort(nums, m, r)
            self.Merge(nums, l, m, r)


    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = {}
        output = [0] * 2

        self.MergeSort(nums, 0, len(nums))

        for i in range(len(nums)):
            d[i+1] = 0

        for i in range(len(nums)):
            d[nums[i]] += 1

        for key, val in d.items():
            if val == 2:
                output[0] = key
            if val == 0:
                output[1] = key
        return output



def test_1():
    sol = Solution()
    nums = [1,2,2,4]
    output = [2, 3]
    assert sol.findErrorNums(nums) == output

def test_2():
    sol = Solution()
    nums = [1,1]
    output = [1, 2]
    assert sol.findErrorNums(nums) == output
