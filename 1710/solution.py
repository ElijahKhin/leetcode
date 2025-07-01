from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxes = sorted(boxTypes, key=lambda item: -item[1])
        res = 0
        for box in boxes:
            if truckSize == 0:
                return res
            if truckSize >= box[0]:
                res += box[0] * box[1]
                truckSize -= box[0]
            else:
                while truckSize > 0:
                    res += box[1]
                    truckSize -= 1 
        return res


def test_1():
    boxTypes = [[1,3],[2,2],[3,1]] 
    truckSize = 4
    output = 8 
    sol = Solution()
    res = sol.maximumUnits(boxTypes, truckSize)
    assert res == output

def test_2():
    boxTypes = [[5,10],[2,5],[4,7],[3,9]]
    truckSize = 10
    output = 91
    sol = Solution()
    res = sol.maximumUnits(boxTypes, truckSize)
    assert res == output

if __name__ == "__main__":
    sol = Solution()
    res = sol.maximumUnits(boxTypes, truckSize)
