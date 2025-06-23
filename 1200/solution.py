from typing import List

class Solution:
    def BubbleSort(self, arr):
        ll = len(arr)
        for i in range(ll):
            swp = False
            for j in range(ll - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j] 
                    swp = True
            if swp == False:
                break

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        self.BubbleSort(arr) 
        # find min diff
        # collect all pairs

        min = 1e9
        res = []
        for i in range(len(arr)- 1):
            mm = abs(arr[i + 1] - arr[i])
            if mm < min:
                min = mm 
        for i in range(len(arr) - 1):
            val = abs(arr[i + 1] - arr[i])
            if val == min:
                res.append([arr[i], arr[i+1]])
        return res


def test_1():
    arr = [4,2,1,3]
    output = [[1,2],[2,3],[3,4]]
    sol = Solution()
    res = sol.minimumAbsDifference(arr)
    assert res == output

def test_2():
    arr = [1,3,6,10,15]
    output = [[1,3]]
    sol = Solution()
    res = sol.minimumAbsDifference(arr)
    assert res == output

def test_3():
    arr = [3,8,-10,23,19,-4,-14,27]
    output = [[-14,-10],[19,23],[23,27]]
    sol = Solution()
    res = sol.minimumAbsDifference(arr)
    assert res == output
