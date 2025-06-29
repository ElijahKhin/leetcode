from typing import List
import math

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = {}
        for i in range(len(arr)):
            key = bin(arr[i])[2:].count('1')
            d.setdefault(key, []).append(arr[i]) 
        d = dict(sorted(d.items()))
        res = []
        for val in d.values():
            val.sort()
            res += val
        return res


def test_1():
    arr = [0,1,2,3,4,5,6,7,8]
    output = [0,1,2,4,8,3,5,6,7]
    sol = Solution()
    res = sol.sortByBits(arr)
    assert res == output

def test_2():
    arr = [1024,512,256,128,64,32,16,8,4,2,1]
    output = [1,2,4,8,16,32,64,128,256,512,1024]
    sol = Solution()
    res = sol.sortByBits(arr)
    assert res == output

