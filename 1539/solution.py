from typing import List

def binSearch(arr: List[int], target: int) -> bool:
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
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        while k > 0:
            if binSearch(arr, i) is not True:
                k -= 1
            i += 1
        return i - 1

if __name__ == "__main__":
    arr = [2,3,4,7,11]
    k = 5 
    output = 9
    sol = Solution()
    res = sol.findKthPositive(arr, k)
    print(res == output)
