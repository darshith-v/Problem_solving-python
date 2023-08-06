def bubble_sort(arr):
    n = len(arr)
    for i in range(n):

        for j in range(i+1,n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


lt =    [89,43,56,90,88,21]

bubble_sort(lt)
print(lt)