nums = [5, 3, 4, 3,3,3,3,3,3,10]

n = len(nums)
for i in range(n):
    swp = False
    for j in range(n - i - 1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            swp = True
    if swp == False:
        break
print(nums)
