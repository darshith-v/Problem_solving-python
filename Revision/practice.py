'''

def coins():
    t = int(input())

    for _ in range(t):
        alice, bob = map(int, input().split())
        maxi = max(alice,bob)
        for i in range(maxi):

            if (alice == 1000000000 and bob == 1000000000):
                break

            if alice >= bob:
                alice -= 1
            else:
                alice, bob = bob, alice
                alice -= 1

            if bob >= alice:
                bob -= 1
            else:
                alice, bob = bob, alice
                bob -= 1

        print(f'{"Alice" if alice > bob else "Bob"}')

coins()


# Find the perfect number between 1 to 100;

count = 0

for i in range(1,100):
  for j in range(1,i):
    if (i % j == 0):
      count += j
  if(count==i):
    print(count)
  count = 0    


'''
# Input value :
# n = 8
# s = DDUUUUDD

# Output Value : 1
'''

def countingValleys(n, s):
    count = 0
    result = 0

    for i in s:
        if(i == 'U'):
            count += 1
        else:
            count -= 1

        if i == 'U' and count == 0:
            result += 1

    return result

num = int(input("Enter the number of steps: "))        
str1 = input("Enter the String: ")

result = countingValleys(num, str1)
print(result)



# Rotation of array

def rotataionArray(arr, k, pos):
    n = len(arr)
    result = []

    def rotation(arr):
        lastElement = arr[n - 1]
        for i in range(n-1, 1, -1):
            arr[i] = arr[i - 1]
        arr[0]  = lastElement

    for i in range(k):
        rotation(arr)

    # get the values at given indices
    
    # result = [arr[i] for i in pos]
    # return result
    for i in pos:
        result.append(arr[i])
    return result    
    

a = list(map(int,(input("enter the array list: ")).split()))   #[1,2,3,4]
k = int(input("enter the no of iteration: "))                  # 2
position = list(map(int,(input("Enter the position of array: ")).split())) #[0,3]

result = rotataionArray(a, k, position)
print(result)                                                      # output: [3, 2]



#4. 
#Given an integer array Arr of size N the task is to find the count of elements whose #value is greater than all of its prior elements.
#Note : 1st element of the array should be considered in the count of the result.
# For example,
# Arr[]={7,4,8,2,9}
# As 7 is the first element, it will consider in the result.
# 8 and 9 are also the elements that are greater than all of its previous elements.
# Since total of  3 elements is present in the array that meets the condition.
# Hence the output = 3.


Arr = []
count = 1
size = int(input("Enter the size of array: "))
for i in range (size):
    n = int(input())
    Arr.append(n)

for i in range(len(Arr)):
    first = Arr[0]
    if Arr[i] > first:
        count = count + 1
print("Output is : ", count)  

# 6.
#A parking lot in a mall has RxC number of parking spaces. Each parking space will #either be  empty(0) or full(1). The status (0/1) of a parking space is represented as #the element of the matrix. The task is to find index of the prpeinzta row(R) in the #parking lot that has the most of the parking spaces full(1).

#Note :
#RxC- Size of the matrix
#Elements of the matrix M should be only 0 or 1.

#Example 1:
#Input :
# 3   -> Value of R(row)
# 3    -> value of C(column)
# [0 1 0 1 1 0 1 1 1] -> Elements of the array M[R][C] where each element is separated  # by new line.
# Output :
# 3  -> Row 3 has maximum number of 1’s

# Example 2:
# input :
# 4 -> Value of R(row)
# 3 -> Value of C(column)
# [0 1 0 1 1 0 1 0 1 1 1 1] -> Elements of the array M[R][C]
# Output :
# 4  -> Row 4 has maximum number of 1’s

row = int(input("Enter the rows: "))
column = int(input("Enter the columns: "))

m = 0
sum = 0
id = 0

for i in range(row):
    for j in range(column):
        sum += int(input())
    if sum > m:
        m = sum
        id = i + 1
    sum = 0
print(id)        


# 5.

#Input 1:
    ###***   -> Value of S
#Output :
#   0   → number of * and # are equal

str = input("Enter '#' or '*': ")
a = 0
b = 0

for i in str:
    if i == '*':
        a += 1
    else:
        b += 1
result = a - b
print(result)            


# 6.

T = int(input())

E = list(map(int, input().split()))
L = list(map(int, input().split()))

current_guests = 0
max_guests = 0

for i in range(T):
    current_guests += E[i]
    current_guests -= L[i]

    if current_guests > max_guests:
        max_guests = current_guests

print(max_guests)



#7. Find the smallest number in an array

num = [7, 0, 8, 6, 3]

minElement = float('inf') # some random big number

for i in range(len(num)):
    minElement = min(minElement, num[i])
print(minElement)  


#8 . Find the biggest number in an array

num = [8, 9, 10, 3, 7]

maxElement = 0

for i in range(len(num)):
    if num[i] > maxElement:
        maxElement = num[i]
print(maxElement)    


# 9 Find the second largest and second smallest element in an array

def largestElement(arr):
    largest = second_largest = float('-inf')
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

def smallestElement(arr):
    smallest = second_smallest = float('inf')        
    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest            

arr = [4, 5, 7, 8, 8, 2]
largeEle = largestElement(arr)
smallEle = smallestElement(arr)

print("The second largest number is ", largeEle)
print("The second smallest number is ", smallEle)


# 10 reverse an array

def reverseArray(arr):
    n = len(arr)
    start, end = 0 , n - 1
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    print(arr)

reverseArray([5, 4, 3, 2, 1])


# 11 reverse a string

str = "Hello world"
empty = ""

for i in range(len(str) - 1, -1 , -1):
    empty += str[i]
print(empty)

'''

# reverse a word or swapping 2 words

str = "Hello world"

space_index = -1

word1 = ""
word2 = ""

for i in range(len(str) - 1):
    if str[i] == " ":
        space_index = i
        break

for i in range(space_index):
    word1 += str[i]

for i in range(space_index, len(str)):
    word2 += str[i]

reverse = word2 +" "+  word1
print(reverse)
