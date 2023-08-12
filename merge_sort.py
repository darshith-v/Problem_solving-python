def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    #divide the array
    mid_idx = len(arr)//2
    left_arr = arr[:mid_idx]
    right_arr = arr[mid_idx:]

    #recursive for divided array
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    return merge(left_arr,right_arr)

def merge(left,right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])  
            j+=1

    result.extend(left[i:])      
    result.extend(right[j:])

    return result


# n = int(input("enter n : "))
# lt = [int(input("enter the element one by one: ")) for i in range(n)]

lt = [45,89,66,23,90,21]

result = merge_sort(lt)
print(result)