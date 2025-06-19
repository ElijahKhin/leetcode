nums = [5, 3, 4]

for i in range(len(nums)):
    swp = False
    for j in range(len(nums) - 1 - i):
        if (nums[j] >= nums[j+1]):
            nums[j], nums[j+1] = nums[j+1], nums[j]
            swp = True
    if swp == False:
        break

print(nums)
