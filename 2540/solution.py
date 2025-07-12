from typing import List

def binSearch(arr, target):
    l = 0 
    r = len(arr)
    while l < r:
        m = l + (r-l) // 2
        if arr[m] == target:
            return True
        elif arr[m] < target:
            l = m + 1
        else:
            r = m
    return False

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)

        for i in range(n1):
            target = nums1[i]
            if binSearch(nums2, target):
                return target
        return -1

if __name__ == "__main__":
    nums1 = [1,2,3,6]
    nums2 = [2,3,4,5]
    output = 2 
    sol = Solution()
    res = sol.getCommon(nums1, nums2)
    print(res)
    print(res == output)
