from typing import List

def sort(nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(1, n):
        j = i - 1 
        val = nums[i]
        while j >= 0 and nums[j] > val:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = val
    return nums


        

if __name__ == "__main__":
    nums = [4,3,1,2]
    sort(nums)
    print(nums)
