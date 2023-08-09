def reverse_array(arr):
    i = 0
    j = (n-1)
    while i < j:
        arr[i],arr[j] = arr[j],arr[i]
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
