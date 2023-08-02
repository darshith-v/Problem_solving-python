def linear_search(arr,target):
    for index, value in enumerate(arr):
        print(index,value)
        if value == target:
            return index
    return -1        


lt = []
n = int(input("enter n : "))
print("enter the elements")

for i in range(0,n):
    lt.append(int(input()))

target_value = int(input("enter the target value: "))    

result = linear_search(lt,target_value)

if result != -1:
    print(f"The target value of {target_value} is present in index of {result}")
else:
    print(f"The target value of {target_value} is not found in list")    