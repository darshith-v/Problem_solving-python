#running sum of array
def running_sum_array(array):

    n = len(array)
    new_list = []
    for i in range(0,n):
        new_list.append(0)                        #if input we give 5 then = [0,0,0,0,0] 

    new_list[0] = list[0]                         #index value 0 is equal to list
    for i in range(1,n):                          #index value start from 1
        new_list[i] = new_list[i - 1] + list[i]
    return new_list

list = []
n = int(input("enter the no of elements: "))

print("enter the elements one by one")
for i in range(0,n):
    list.append(int(input()))


total = running_sum_array(list)
print(total)
