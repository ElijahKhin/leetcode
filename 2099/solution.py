from typing import List
from bisect import bisect_left

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        pairs = list(zip(range(n), nums))
        pairs = sorted(pairs, key=lambda x: (-x[1], x[0]))[:k]
        tmp = [1e6] * n
        for i in range(k):
            tmp[pairs[i][0]] = pairs[i][1]
        res = []
        for i in range(n):
            if tmp[i] != 1e6:
                res.append(tmp[i])
        return res


if __name__ == "__main__":
    k = 2 
    nums = [3,4,3,3] 
    output = [3,4] 
    sol = Solution()
    res = sol.maxSubsequence(nums, k)
    print(res)
    print(res == output)
