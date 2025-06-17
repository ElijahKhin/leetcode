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

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        i = j = 0
        self.MergeSort(nums1, 0, len(nums1))
        self.MergeSort(nums2, 0, len(nums2))

        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res



if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2]
    sol = Solution()
    res = sol.intersect(nums1, nums2)
    print(res)
