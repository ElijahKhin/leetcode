from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        srtarr = list(sorted(set(arr)))
        d = {}
        for i in range(len(srtarr)):
            if d.get(srtarr[i],0) == 0:
                d[srtarr[i]] = i+1
        res = []
        for i in arr:
            res.append(d[i])
        return res

def test_1():
    arr = [40,10,20,30]
    output = [4,1,2,3]
    sol = Solution()
    res = sol.arrayRankTransform(arr)
    assert res == output

def test_2():
    arr = [100,100,100]
    output = [1,1,1]
    sol = Solution()
    res = sol.arrayRankTransform(arr)
    assert res == output

def test_3():
    arr = [37,12,28,9,100,56,80,5,12]
    output = [5,3,4,2,8,6,7,1,3]
    sol = Solution()
    res = sol.arrayRankTransform(arr)
    assert res == output
