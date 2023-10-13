def binary_search(arr, num):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return -1

 
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = 4

index = binary_search(arr, num)
print("Индекс элемента:", index)