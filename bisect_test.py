from bisect import bisect_left

def my_bisect(nums, target):
    idx = bisect_left(nums, target)
    if idx < len(nums) and nums[idx] == target:
        return idx
    else:
        return -1

if __name__ == "__main__":
    nums = [6,7,8,5]
    print(my_bisect(nums, 3))
