def Is_array_sorted(arr):
    n = len(arr)
    for i in range(1,n):
        if arr[i] < arr[i - 1]:
            return False
        return True        

lt = []    
n = int(input("enter n : "))
print("enter element one by one")

for i in range(0,n):
    lt.append(int(input()))

print(lt)    

if Is_array_sorted(lt):
    print("yes the array is sorted")
else:
    print("No the array is not sorted")    