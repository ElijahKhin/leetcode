from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nl = len(nums1)
        nr = len(nums2)
        ns = nl + nr
            
        i = j = 0

        arr = [0] * (ns)
        while i < nl and j < nr:
            if nums1[i] < nums2[j]:
                arr[i + j] = nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                arr[i + j] = nums2[j]
                j += 1
            else:
                arr[i + j] = nums1[i]
                i += 1
                arr[i+j] = nums2[j]
                j += 1

        while i < nl:
            arr[i+j] = nums1[i]
            i += 1

        while j < nr:
            arr[i+j] = nums2[j]
            j += 1
        
        return arr[ns // 2] if ns % 2 == 1 else (arr[ns // 2 - 1] + arr[ns // 2]) / 2

if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [3,4]

    sol = Solution()
    print(sol.findMedianSortedArrays(nums1, nums2))
