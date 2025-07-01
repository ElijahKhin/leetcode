from typing import List

class Solution:
    def Merge(self, nums, l, m, r):
        nl = m - l
        nr = r - m
        lhs = [0] * nl
        rhs = [0] * nr

        for i in range(nl):
            lhs[i] = nums[l+i]

        for i in range(nr):
            rhs[i] = nums[m+i]
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

    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        self.MergeSort(nums, 0, n)

        res = 0
        l, r = 0, n - 1
        while l <= r:
            summ = nums[l] + nums[r] 
            if summ <= target:
                res += 2 ** (r - l)
                l += 1
            else:
                r -= 1
        return int((res) % (1e9 + 7))



def test_1():
    nums = [3,5,6,7]
    target = 9 
    output = 4 
    sol = Solution()
    res = sol.numSubseq(nums, target)
    assert res == output

def test_2():
    nums = [3,3,6,8]
    target = 10 
    output = 6 
    sol = Solution()
    res = sol.numSubseq(nums, target)
    assert res == output

def test_3():
    nums = [7,6,4,3,3,2]
    target = 12 
    output = 61 
    sol = Solution()
    res = sol.numSubseq(nums, target)
    assert res == output

if __name__ == "__main__":
    nums = [3,5,6,7]
    target = 9 
    output = 4
    sol = Solution
    res = sol.numSubseq(nums, target)
