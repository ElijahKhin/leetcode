from typing import List

class Solution:
    def Merge(self, arr, l, m, r):
        nl = m - l
        nr = r - m

        lhs = [0] * nl
        rhs = [0] * nr

        for i in range(nl):
            lhs[i] = arr[l + i]

        for i in range(nr):
            rhs[i] = arr[m + i]
        
        i = j = 0
        k = l
        while i < nl and j < nr:
            if lhs[i] < rhs[j]:
                arr[k] = lhs[i]
                i += 1
            else:
                arr[k] = rhs[j]
                j += 1
            k += 1

        while i < nl:
            arr[k] = lhs[i]
            i += 1
            k += 1

        while j < nr:
            arr[k] = rhs[j]
            j += 1
            k += 1

    def MergeSort(self, arr, l, r):
        if r - l > 1:
            m = l + (r - l) // 2
            self.MergeSort(arr, l, m)
            self.MergeSort(arr, m, r)
            self.Merge(arr, l, m, r)

    def arrayPairSum(self, nums: List[int]) -> int:
        self.MergeSort(nums, 0, len(nums))
        res = 0
        for i in range(1, len(nums), 2):
            res += min(nums[i-1], nums[i])
        return res


def test_1():
    sol = Solution()
    nums = [1,4,3,2]
    res = sol.arrayPairSum(nums)
    
    assert res == 4 

def test_2():
    sol = Solution()
    nums = [6,2,6,5,1,2]
    res = sol.arrayPairSum(nums)
    
    assert res == 9
