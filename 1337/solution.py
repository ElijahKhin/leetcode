from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = {}
        for i in range(len(mat)):
            d[i] = sum(mat[i])
        d = dict(sorted(d.items(), key=lambda x: x[1]))
        print(d)
        res = []
        for i,j in zip(range(k),d.keys()):
            res.append(j)
        return res

def test_1():
    mat = [[1,1,0,0,0],
           [1,1,1,1,0],
           [1,0,0,0,0],
           [1,1,0,0,0],
           [1,1,1,1,1]]
    k = 3
    output = [2,0,3]
    sol=Solution()
    res = sol.kWeakestRows(mat, k)
    assert res == output

def test_2():
    mat = [[1,0,0,0],
           [1,1,1,1],
           [1,0,0,0],
           [1,0,0,0]]    
    k = 2
    output = [0,2]
    sol=Solution()
    res = sol.kWeakestRows(mat, k)
    assert res == output
