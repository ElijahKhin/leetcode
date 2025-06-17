from typing import List

class Solution:
    def Merge(self, arr, l, m, r):
        nl = m - l 
        nr = r - m

        lhs = [0] * nl
        rhs = [0] * nr

        for i in range(nl):
            lhs[i] = arr[l + i]

        for i in range(nr):
            rhs[i] = arr[m + i]

        i = j = 0
        k = l

        while i < nl and j < nr:
            if lhs[i] < rhs[j]:
                arr[k] = lhs[i]
                i += 1
            else:
                arr[k] = rhs[j]
                j += 1
            k += 1

        while i < nl:
            arr[k] = lhs[i]
            i += 1
            k += 1

        while j < nr:
            arr[k] = rhs[j]
            j += 1
            k += 1
            

    def MergeSort(self, arr, l, r):
        if r - l > 1:
            m = l + (r - l) // 2
            self.MergeSort(arr, l, m)
            self.MergeSort(arr, m, r)
            self.Merge(arr, l, m, r)

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        self.MergeSort(nums, 0, len(nums))

        output = 1e9
        sums = {}
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                diff = abs(target - s)
                sums[s] = diff
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                if target - s >= 0:
                    l += 1
                else:
                    r -= 1
        mmin = min(sums.values())
        for key, value in sums.items():
            if value == mmin:
                return key

def test_1():
    sol = Solution()
    nums = [-1,2,1,-4]
    target = 1 
    output = 2
    assert sol.threeSumClosest(nums, target) == output

def test_2():
    sol = Solution()
    nums = [0,0,0]
    target = 1 
    output = 0
    assert sol.threeSumClosest(nums, target) == output

if __name__ == "__main__":
    sol = Solution()
    nums = [-4, -1, 1, 2]
    target = 1 
    output = 2
    sol.threeSumClosest(nums, target)


