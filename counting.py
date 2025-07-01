def CountingSort(nums):
    mx = max(nums) + 1
    cntA = [0] * mx

    n = len(nums) 
    for i in range(n):
        cntA[nums.pop()] += 1

    for i in range(mx):
        if cntA[i] > 0:
            nums.extend([i] * cntA[i])
    print(nums)


def test_1():
    nums = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
    srt_nums = [1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6]
    CountingSort(nums)
    assert srt_nums == nums 
