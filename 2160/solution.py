from typing import List

class Solution:
    def InsertionSort(self, arr: List[int]) -> int:
        for i in range(1, 4):
            val = arr[i]
            j = i - 1 
            while j >= 0 and arr[j] > val:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = val


    def minimumSum(self, num: int) -> int:
        arr = []
        while num > 0:
            arr.append(num % 10)
            num //= 10
        self.InsertionSort(arr)

        return arr[0] * 10 + arr[2] + arr[1] * 10 + arr[3]


if __name__ == "__main__":
    num = 4009 
    output = 13
    sol = Solution()
    res = sol.minimumSum(num)
    print(res) 
    print(res == output)
