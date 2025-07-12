from typing import List

def binary_search_left(arr: List[int], target: int) -> int:
    l = 0
    r = len(arr)
    while l < r:
        m = l + (r-l) // 2
        if arr[m] < target:
            l = m+ 1
        else:
            r = m
    if l < len(arr) and arr[l] == target:
        return l
    return -1

if __name__ == "__main__":
    arr = [1, 2, 2, 2, 3, 4]
    target = 2
    res = binary_search_left(arr, target)
    print(res)
