def move_zeros(arr):
    n = len(arr)

    ct = 0                    #creating new variable index value as 0
    for i in range(0,n):
        if arr[i] != 0:
            t = arr[i]
            arr[i] = arr[ct]
            arr[ct] = t
            ct+=1


lt = []
n = int(input("enter n : "))
print("enter the element one by one")

for i in range(0,n):
    lt.append(int(input()))

move_zeros(lt)
print(lt)