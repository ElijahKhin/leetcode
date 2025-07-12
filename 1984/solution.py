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

    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        self.MergeSort(nums, 0, n)
        if k == 1:
            return 0
        mm = -1
        loop = 0
        while loop < n - k + 1:
            val = nums[loop + k - 1] - nums[loop]
            if val < mm or mm == -1:
                mm = val
            loop += 1
        return mm




if __name__ == "__main__":
    nums = [9,4,1,7]
    k = 2
    sol = Solution()
    res = sol.minimumDifference(nums, k)
    print(res)
