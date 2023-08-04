def binary_search(arr,key):
    n = len(arr)
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end)//2

        if arr[mid] == key:
            return mid

        elif arr[mid] > key:
            end = mid - 1     

        elif arr[mid] < key:
            start = mid + 1
    return -1


lt = []
n = int(input("enter n : "))
print('enter elements one by one')

for index in range(0,n):
    lt.append(int(input()))

key_value = int(input("key value is: "))

result = binary_search(lt, key_value)

if result != -1:
    print(f"The given key {key_value} is present in index of {result}")
else:
    print(f"The given key {key_value} is not present in list")    