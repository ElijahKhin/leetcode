from typing import List

class Solution:
    def merge(self, nums, l, m , r):
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

    def mergeSort(self, nums, l, r):
        if r - l > 1:
            m = l + (r-l) // 2
            self.mergeSort(nums, l, m)
            self.mergeSort(nums, m, r)
            self.merge(nums, l, m, r)

    def binSearch(self, nums, target):
        l = 0
        r = len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m
        idx = l - 1
        if 0 <= idx <= len(nums) and nums[idx] <= target:
            return idx
        return -1

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        self.mergeSort(nums, 0, n)
        pref_sum = [0] * n
        for i in range(n):
            if i == 0:
                pref_sum[0] = nums[0]
            else:
                pref_sum[i] = pref_sum[i-1] + nums[i]
        answer = [0] * len(queries)
        for i, target in enumerate(queries):
            val = self.binSearch(pref_sum, target)
            if val == -1:
                answer[i] = 0
            else:
                answer[i] = val + 1
            
        return answer







if __name__ == "__main__":
    nums = [624082]
    queries = [972985,564269,607119,693641,787608,46517,500857,140097]
    output = [1,0,0,1,1,0,0,0]
    sol = Solution()
    answer = sol.answerQueries(nums, queries)
    print(answer)
    print(answer == output)
