from typing import List

def selection(nums: List[int]) -> None:
    n = len(nums)
    for i in range(n):
        mm = i
        for j in range(1+i, n):
            if nums[j] < nums[mm]:
                mm = j
        nums[i], nums[mm] = nums[mm], nums[i]

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

