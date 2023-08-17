def partition (arr, first, last):
    pivot = arr[last]
    left_idx = first - 1
    right_idx = first

    while right_idx < len(arr):
        if arr[right_idx] < pivot:
            left_idx += 1
            arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]
        right_idx += 1

    arr[left_idx + 1], arr[last] = arr[last], arr[left_idx + 1]       
    return left_idx + 1

def quick_sort(arr, first, last):
    if first < last :
        pi = partition(arr, first, last)
        quick_sort(arr, first, pi - 1)
        quick_sort(arr, pi + 1, last)

arr = [14,1,14,100,5,17]        
n = len(arr)
quick_sort(arr, 0, n-1)
print(arr)