from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        d = dict.fromkeys(nums, -1)
        for i in range(n):
            idx = d[nums[i]]
            if idx != -1 and abs(i - idx) <= k:
                return True 
            else:
                if idx == -1 or i > idx:
                    d[nums[i]] = i
        return False

            

