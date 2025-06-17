def merge(nums, l, m, r):
    lhs = [0] * (m - l)
    rhs = [0] * (r - m)

    for i in range(m - l):
        lhs[i] = nums[l + i]

    for i in range(r - m):
        rhs[i] = nums[m+i]

    print(lhs)
    print(rhs)

    i = j = 0
    k = l
    while i < len(lhs) and j < len(rhs):
        if lhs[i] > rhs[j]:
            nums[k] = rhs[j]
            j += 1
        else:
            nums[k] = lhs[i]
            i += 1
        k += 1

    while i < len(lhs):
        nums[k] = lhs[i]
        i += 1
        k += 1
    
    while j < len(rhs):
        nums[k] = rhs[j]
        j += 1
        k += 1

def merge_sort(nums, l, r):
    if r - l > 1:
        m = l + (r - l) // 2
        merge_sort(nums, l, m)
        merge_sort(nums, m, r)
        merge(nums, l, m, r)

if __name__ == "__main__":
    nums = [1, 5, 23, 43, -1, 0, 2, 10]

    merge_sort(nums, 0, len(nums))
    print(nums)

