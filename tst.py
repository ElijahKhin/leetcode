from bisect import bisect_left

def binarySearchLeft(nums, target):
    idx = bisect_left(nums, target)
    if nums[idx] == target:
        return idx
    else:
        return -1

if __name__ == "__main__":
    nums = [1,2,2,2,2,3,4,5]
    target = 0
    print(binarySearchLeft(nums, target))
    

