from typing import List

def binary_search_right(arr: List[int], target: int) -> int:
    l = 0
    r = len(arr)
    while l < r:
        m = l + (r-l) // 2
        if arr[m] <= target:
            l = m + 1
        else:
            r = m
    idx = r - 1
    if 0 <= idx < len(arr) and arr[idx] == target:
        return r - 1
    return -1

if __name__ == "__main__":
    arr = [1, 2, 2, 2, 3, 4]
    target = 2 
    res = binary_search_right(arr, target)
    print(res)
