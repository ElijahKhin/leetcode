from typing import List

class Solution:
    def Merge(self, nums, l, m, r):
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

    def MergeSort(self, nums, l, r):
        if r - l > 1:
            m = l + (r - l) // 2
            self.MergeSort(nums, l, m)
            self.MergeSort(nums, m, r)
            self.Merge(nums, l, m, r)

    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [i ** 2 for i in nums]
        self.MergeSort(nums, 0, len(nums))
        print(nums)
        return nums 

def test_1():
    nums = [-4,-1,0,3,10]
    output = [0,1,9,16,100]

    sol = Solution()
    res = sol.sortedSquares(nums)

    assert res == output

def test_2():
    nums = [-7,-3,2,3,11]
    output = [4,9,9,49,121]

    sol = Solution()
    res = sol.sortedSquares(nums)

    assert res == output

if __name__ == "__main__":
    nums = [0, 0, -1, 2, 5, -5]
    sol = Solution()
    sol.MergeSort(nums, 0, len(nums))
    print(nums)
