def simple_array_sum(arr):
    total = 0
    i = 0
    while i < len(arr):
        total += arr[i]
        i+=1
    return total    


my_list = [3,1,6,8,9,4]    
result = simple_array_sum(my_list)
print(result)