#create a empty array
array = []
evenArr = []
oddArr = []
n = int(input("enter the size of array: "))

#appending the values to the array
for i in range(0,n):
    number = int(input("enter the value: "))
    array.append(number)    
    
    if i % 2 == 0:
        evenArr.append(array[i])
    else:
        oddArr.append(array[i])    

#sorted even and odd in order
evenArr = sorted(evenArr)
print(evenArr[0:len(evenArr)])

oddArr = sorted(oddArr)
print(oddArr[0:len(evenArr)])

#adding second largest number in both matrix
final_sum = evenArr[-2] + oddArr[-2]
print("The sum of second largest values: ",final_sum)