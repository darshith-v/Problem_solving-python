def merge_sort(arr):
    if len(arr) > 1:

        #Divide the array into two halves
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        #recursion sort both halves
        merge_sort(left_arr)
        merge_sort(right_arr)

        i,j,k = 0, 0, 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
                k+=1
            else:
                arr[k] = right_arr[j]
                j+=1
                k+=1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1
    ''' 
    #if last element remains to add for arr[k]
    arr[k].extend(arr[left_arr]:)
    arr[k].extend(arr[right_arr]:)
    '''

n = int(input("enter n : "))
lt = [int(input("enter the element one by one: ")) for i in range(n)]

result = merge_sort(lt)
print(result)