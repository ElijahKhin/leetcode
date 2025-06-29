arr = [23, 34, 1, 23, 25, 89, 2, 55, 3, 7, 23, 0, -23, -1]

for i in range(1, len(arr)):
    val = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > val:
        arr[j + 1] = arr[j]     # сдвигаем вправо
        j -= 1
    arr[j + 1] = val            # вставляем
