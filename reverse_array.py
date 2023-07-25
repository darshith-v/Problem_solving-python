def reverse_array(arr):
    i = 0
    j = (n-1)
    while i < j:
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t
        i += 1
        j-=1
    return arr    

lt = []
n = int(input("enter n elements: "))
print("enter the elements one by one")

for i in range(0,n):
    lt.append(int(input()))

print(lt)    
print(reverse_array(lt))