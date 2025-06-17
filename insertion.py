arr = [23, 34, 1, 23, 25, 89, 2, 55, 3, 7, 23, 0, -23, -1]

for i in range(1, len(arr)):
    j = i - 1
    val = arr[i]
    while arr[j] > val and j >= 0:
        arr[j], arr[j+1] = val, arr[j]
        j-=1
print(arr)
