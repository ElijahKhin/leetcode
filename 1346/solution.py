from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {}
        for i in range(len(arr)):
            d[i] = arr[i]
        lst = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
        print(lst)
        for key1, val1 in lst.items():
            for key2, val2 in lst.items():
                if key1 != key2:
                    if val1 == val2*2 or val2 == val1*2:
                        return True
        return False

if __name__ == "__main__":
    arr = [10,2,5,3]
    sol = Solution()
    print(sol.checkIfExist(arr))
