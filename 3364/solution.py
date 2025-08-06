from typing import List

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix[i] = prefix[i-1] + nums[i-1]
        print(prefix)

        mm = 1e7
        for right in range(l, r + 1):
            for left in range(n + 1 - right):
                val = prefix[left+right] - prefix[left]
                if mm > val > 0:
                    mm = val
        if mm == 1e7:
            return -1
        return mm

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    l = 2
    r = 3
    sol = Solution()
    print(sol.minimumSumSubarray(nums, l, r))
