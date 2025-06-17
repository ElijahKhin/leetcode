from typing import List

class Solution:
    def Merge(self, a, l, m, r):
        lhs = [0] * (m - l)
        rhs = [0] * (r - m)

        for i in range(m - l):
            lhs[i] = a[l+i]
        for i in range(r - m):
            rhs[i] = a[m+i]
        i = 0
        j = 0
        k = l
        while i < m-l and j < r - m:
            if lhs[i] < rhs[j]:
                a[k] = rhs[j]
                j += 1
            else:
                a[k] = lhs[i]
                i += 1
            k += 1
        while i < m-l:
            a[k] = lhs[i]
            i += 1
            k += 1

        while j < r-m:
            a[k] = rhs[j]
            j += 1
            k += 1

    def MergeSort(self, a, l, r):
        if r - l > 1:
            m = l + (r - l) // 2
            self.MergeSort(a, l, m)
            self.MergeSort(a, m, r)
            self.Merge(a, l, m, r)

    def containsduplicate(self, nums: list[int]) -> bool:
        nums = self.MergeSort(nums, 0, len(nums))
        print(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True;
        return False

if __name__ == "__main__":
    a = [1, 5, 23, 43, -1, 0, 2, 10]
    sol = Solution();
    
  #  res = sol.containsDuplicate(nums)
    sol.MergeSort(a, 0, len(a))
    print(a)
