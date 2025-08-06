from collections import deque
from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        prev = False
        n = len(arr)
        hld = deque()
        print(arr)
        for i in range(n):
            if len(hld) > 0:
                hld.append(arr[i])
                arr[i] = hld.popleft()
            if arr[i] == 0:
                prev = True
            else:
                if prev:
                    hld.append(arr[i])
                    arr[i] = 0
                prev = False
            print(hld)


if __name__ == "__main__":
    arr = [1,0,2,3,0,4,5,0]
    output = [1,0,0,2,3,0,0,4]
    sol = Solution()
    sol.duplicateZeros(arr)
    print(arr)
