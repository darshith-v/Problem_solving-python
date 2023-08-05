def selection_sort(array,size):
    
    for step in range(0,size):
        min_id = step

        for i in range(step + 1,size):
            if array[i] < array[min_id]:
                min_id = i 

        (array[step], array[min_id]) = (array[min_id], array[step])        

lt = [39,48,57,1,46,45,90]
n = len(lt)
selection_sort(lt,n)
print(lt)
