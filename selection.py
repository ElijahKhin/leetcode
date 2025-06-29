from typing import List

def selection(nums: List[int]) -> None:
    n = len(nums)
    for i in range(n - 1):          # последний элемент уже будет минимальным
        min_idx = i                 # индекс минимального в неотсортированной части
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        if min_idx != i:            # лишнюю перестановку избегаем
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

def test_1():
    nums = [-1,-1,-1,0,0,1,-1,2,-2,5,6,6,8]
    output = nums.copy()
    output.sort()
    selection(nums)
    assert nums == output


if __name__ == "__main__":
    nums = [-1,-1,-1,0,0,1,-1,2,-2,5,6,6,8]
    selection(nums)
    print(nums)

