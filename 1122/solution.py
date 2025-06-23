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


    def MergeSort(self, nums, l, r):
        if r - l > 1:
            m = l + (r - l) // 2
            self.MergeSort(nums, l, m)
            self.MergeSort(nums, m, r)
            self.Merge(nums, l, m, r)

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        self.MergeSort(arr1, 0, len(arr1))
        d = {}
        res = []
        for i in range(len(arr1)):
            d[arr1[i]] = d.get(arr1[i], 0) + 1
        for i in arr2:
            res += [i] * d[i]
            del d[i]
        for key in d.keys():
            res += [key] * d[key]
        return res
        
def test_1():
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    output = [2,2,2,1,4,3,3,9,6,7,19]
    sol = Solution()
    assert output == sol.relativeSortArray(arr1, arr2)

def test_2():
    arr1 = [28,6,22,8,44,17]
    arr2 = [22,28,8,6]
    output = [22,28,8,6,17,44]
    sol = Solution()
    assert output == sol.relativeSortArray(arr1, arr2)
