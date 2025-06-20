from typing import List

class Solution:
    def allCellsDistOrder(self, rows:int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:

def test_1():
    sol = Solution()
    rows = 1 
    cols = 2 
    rCenter = 0 
    cCenter = 0 
    output = [[0,0], [0,1]]
    res = sol.allCellsDistOrder(rows, cols, rCenter, cCenter)
    assert res == output

def test_2():
    sol = Solution()
    rows = 2 
    cols = 2 
    rCenter = 0
    cCenter = 1 
    output1 = [[0,1],[0,0],[1,1],[1,0]]
    output2 = [[0,1],[1,1],[0,0],[1,0]]
    res = sol.allCellsDistOrder(rows, cols, rCenter, cCenter)
    assert res == output1 or res = output2

def test_3():
    sol = Solution()
    rows = 2 
    cols = 3
    rCenter = 1
    cCenter = 2 
    output1 = [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
    output2 = [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]]
    res = sol.allCellsDistOrder(rows, cols, rCenter, cCenter)
    assert res == output1 or res = output2
