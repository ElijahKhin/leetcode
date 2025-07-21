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
            m = l + (r - l) // 2
            self.MergeSort(nums, l, m)
            self.MergeSort(nums, m, r)
            self.Merge(nums, l, m, r)

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        n = len(digits)
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j or digits[k] % 2 == 1:
                        continue
                    val = digits[i] * 100 + digits[j] * 10 + digits[k] 
                    res.add(val)
        res = list(res)
        self.MergeSort(res, 0, len(res))
        return res

if __name__ == "__main__":
    digits = [2,1,3,0]
    output = [102,120,130,132,210,230,302,310,312,320]
    sol = Solution()
    res = sol.findEvenNumbers(digits)
    print(res)
    print(res == output)

