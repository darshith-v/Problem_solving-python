def maximum(arr):
    n = len(arr)
   
    #for maximum value
    mx = 0
    for i in range(1,n):
        arr[i] > mx
        mx = arr[i]
    return mx    
    
def missing_num(arr):     
    n = len(arr)
    p = maximum(arr)
    sum1 = (p * (p + 1)) // 2
    sum2 = 0
    for i in range(0,n):           #sum of array
        sum2 += arr[i]    
    return (sum1 - sum2)

lt = []    
n = int(input("enter n : "))
print("enter element one by one")

for i in range(0,n):
    lt.append(int(input()))

result = missing_num(lt)   
print("The missing number is : ",result)
