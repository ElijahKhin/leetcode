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
                nums[k] = rhs[j]
                j += 1
            else:
                nums[k] = lhs[i]
                i += 1
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


    def InsertionSort(self, nums):
        n = len(nums)
        for i in range(1, n):
            val = nums[i]
            j = i - 1
            while j >=0 and nums[j] < val:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                j -= 1

    def BubbleSort(self, nums):
        n = len(nums)
        for i in range(n):
            swp = False
            for j in range(n - i - 1):
                if nums[j] < nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swp = True
            if swp == False:
                break

    def SelectionSort(self, nums):
        n = len(nums)
        for i in range(n):
            max = i
            for j in range(i+1, n):
                if nums[j] > nums[max]:
                    max = j
            if max != i:
                nums[i], nums[max] = nums[max], nums[i]


    def minSubsequence(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.MergeSort(nums, 0, n)
        ssum = sum(nums)
        res = [nums[0]]
        accum = sum(res)
        for i in range(1, n):
            if accum > ssum - accum:
                return res
            else:
                res.append(nums[i])
                accum = sum(res)
        return res

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
                nums[k] = rhs[j]
                j += 1
            else:
                nums[k] = lhs[i]
                i += 1
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


    def InsertionSort(self, nums):
        n = len(nums)
        for i in range(1, n):
            val = nums[i]
            j = i - 1
            while j >=0 and nums[j] < val:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                j -= 1

    def BubbleSort(self, nums):
        n = len(nums)
        for i in range(n):
            swp = False
            for j in range(n - i - 1):
                if nums[j] < nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swp = True
            if swp == False:
                break

    def SelectionSort(self, nums):
        n = len(nums)
        for i in range(n):
            max = i
            for j in range(i+1, n):
                if nums[j] > nums[max]:
                    max = j
            if max != i:
                nums[i], nums[max] = nums[max], nums[i]


    def minSubsequence(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.MergeSort(nums, 0, n)
        ssum = sum(nums)
        res = [nums[0]]
        accum = sum(res)
        for i in range(1, n):
            if accum > ssum - accum:
                return res
            else:
                res.append(nums[i])
                accum = sum(res)
        return res





def test_1():
    nums = [4,3,10,9,8]
    output = [10,9]
    sol = Solution()
    res = sol.minSubsequence(nums)
    assert res == output

def test_2():
    nums = [4,4,7,6,7]
    output = [7,7,6]
    sol = Solution()
    res = sol.minSubsequence(nums)
    assert res == output

if __name__ == "__main__":

    nums1 = [4,3,10,9,8] # 3 4 8 9 10
    nums2 = [4,4,7,6,7]
    sol = Solution()
    res = sol.minSubsequence(nums1)
