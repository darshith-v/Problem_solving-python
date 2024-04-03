'''

#1
def solveMefirst(a,b):
  return a + b;

num1 =  int(input())
num2 = int(input())
res = solveMefirst(num1,num2)
print(res)

#2
def simpleArraySum(arr):
  return sum(arr)


myArray = [1,2,3,4,5];
print(simpleArraySum(myArray));

#3
def campareTriplets(a,b):
  alice = 0
  bob = 0

  for i in range(3):
    if a[i] > b[i]:
      alice+=1
    elif a[i] < b[i]:
      bob+=1
  return alice, bob;    
  
array1 = 5, 6, 7
array2 = 3, 6, 10

print(campareTriplets(array1, array2));

#4
def aVeryBigSum(ar):
  return sum(ar)

a1 = 100000002
a2 = 100000003
a3 = a2, a1
result = aVeryBigSum(a3);
print(result);


#5

def diagonalDifferce(arr):
  leftdiag = rightdiag = 0
  for i in range(n):
    leftdiag = leftdiag + arr[i][i]
    rightdiag = rightdiag + arr[i][n - 1 - i]
  return abs(leftdiag - rightdiag);


n = int(input().strip())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().rstrip().split())))

print(diagonalDifferce(arr));

#6

def hashPattern(n):
  for i in range(1, n + 1):
    s = "#" * i; 
    print(s.rjust(n))
  

n = int(input())
result = hashPattern(n);
print(result)


# 7

def miniMaxSum(arr):
  s = 0
  minnum = 999999999999
  maxnum = 0

  n = len(arr)
  for i in range(n):
    s = s + arr[i]
    minnum = min(minnum, arr[i])
    maxnum = max(maxnum, arr[i])
  print(s-maxnum, s-minnum);

arr = [1,3,5,7,9];
print(miniMaxSum(arr))



#8

def birthdayCakeCandles(arr):
  
  n = len(arr)
  maxnum = 0
  count = 0
  for i in range(n):
    if(arr[i] > maxnum):
      maxnum = arr[i]
      count = 1
    elif arr[i] == maxnum:
      count+=1
  return count
  # return arr.count(max(arr)) #another method

print(birthdayCakeCandles([4,4,1,3]));

#9

def timeComversion(time):
  meridian = time[-2:]
  if meridian == 'AM' and time[:2] == '12':
    time = '00' + time[2:]
  if meridian == 'PM' and time[:2]!= '12' :
    time = str(12 + int(time[:2])) + time[2:]
  return time

result = '07:05:45PM'
print(timeComversion(result));



def fibonacci_recursive(n):
    if n <= 0:
        return "Please enter a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage
n = 10
print(f"The {n}th Fibonacci number is: {fibonacci_recursive(n)}")

#febonacci in another method

def febonacci(num):
  a = 0
  b = 1
  if num <= 0:
    return "please enter a positive integer"
  else:  
    for i in range(num):
      print(a)
      c = a + b
      a = b
      b = c
    return c

# print(febonacci(9))


def palidroma(n):
  rem = 0
  sum = 0
  while(n > 0):
    rem = n % 10
    sum = sum * 10 + rem
    n = n // 10
  return sum

def main():
  n = int(input("enter your number: "))
  m = palidroma(n)
  if(n == m):
    print("Its is a palidroma number")
  else:
    print("its not a palidroma")  
    
  
  p = int(input("enter your number: "))
  o = febonacci(p)
  
main()


'''
'''

# factorial number
def factorial(num):
  result = 1
  for i in range(1, num+1):
    result = result * i
  return result

print(factorial(5))


def perfect_number(n):
  sum = 0
  for i in range(1, n):
    if(n % i == 0):
      sum += i
  return sum    

def main():
  n = int(input("enter your number: "))
  m = perfect_number(n)
  if(n == m):
    print("it is a perfect number")
  else:
    print("it's not a perfect number")  

main()

#sum of digit given number  

def sum_digit(num):
  sum = 0
  while(num > 0):
    remainder = num % 10
    sum = sum + remainder
    num = num // 10
  return sum

def main():
  n = int(input("enter your number: "))
  print(sum_digit(n))
  
main()  

# Prime number

def prime_num(num):
  count = 0
  for i in range(1,num + 1):
    if(num % i == 0):
      count = count + 1
  return count

def main():
  n = int(input("enter num: "))
  m = prime_num(n)

  if(m == 2):
    print("prime number")
  else: 
    print("not a prime number")  

main()    
    
# Range of prime number    
  
def prime_num(num):
  count = 0
  for i in range(1,num + 1):
    if(num % i == 0):
      count = count + 1

  if(count == 2):
    return 1
  else: 
    return 0  

def main():
  n = int(input("from: "))
  m = int(input("to: "))

  for i in range(n, m+1):
    result = prime_num(i)
    if(result == 1):
      print(i)
      

main()

# strong number program
def strong_num(num):
  temp = num
  sum = 0
  while(num > 0):
    rem = num % 10
    fact = 1
    for i in range(rem, 1, -1): #range(start, stop, step)
      fact = fact * i
    sum += fact
    num = num // 10

  if(sum == temp):
    return True
  else:
    return False

def main():
  n = int(input("enter the number: "))
  k = int(input("enter the last number: "))

  for i in range(n, k+1):
    m = strong_num(i)
    if(m == True):
      print(i)



  # if (n == m):
  #   print("it is a strong number")
  # else:
  #   print("it is not a strong number")

main()


def perfect_num(num):
  temp = num
  sum = 0
  for i in range(1, num):
    if(num % i == 0):
      sum += i
  if(temp == sum):
    return True
  else:
    return False

def main() :
  n = int(input("enter from number: "))
  m = int(input("enter last number: "))

  for i in range(n, m+1):
    k = perfect_num(i)
    if(k == True):
      print(i)

main()    

# find a number is arm strong or not
def armStrong_num(num):
  sum = 0
  while(num > 0):
    rem = num % 10
    sum += (rem ** 3)
    num = num // 10
  return sum

def main():
  n = int(input("enter the number: "))
  m = armStrong_num(n)
  if(n == m):
    print("Its is an arm strong number: ")
  else:
    print("Its not a arm strong number")  

main()    


# range of armstrong number
def armStrong_num(num):
  temp = num
  sum = 0
  while(num > 0):
    rem = num % 10
    sum += (rem ** 3)
    num = num // 10
  if(sum == temp):
    return True
  else:
    return False  

def main():
  n = int(input("enter the from number: "))
  m = int(input("enter the to number: "))

  for i in range(n, m + 1):
    m = armStrong_num(i)
    if(m == True):
      print(i)  

main()

#reverse the number

def reverse_num(num):
  sum = 0
  while(num > 0):
    rem = num % 10
    sum = sum * 10 + rem
    num = num // 10
  return sum

def main():
  n = int(input("enter the numbers: "))
  print(reverse_num(n))

main()

# factorial of given number using recursive function

def fact_recursion(num):
  if(num == 0):
    result = 1
  else:
    result = num * fact_recursion(num - 1)
    
  return result  

def main():
  n = int(input("enter the number: "))
  m = fact_recursion(n)
  print(m)

main()  

# fibonacci of given number using recursive function

def fibonacci_recursive(num):
  res = 1
  if(num == 0):
    return "Invalid number, give number more than 0"
  elif(num == 1):
    res = 0
  elif(num == 2):
    res = 1
  else:
    res = fibonacci_recursive(num - 1)  + fibonacci_recursive(num - 2)

  return res

def main():
  n = int(input("enter the position of number you want to display in a fibonacci series: "))
  m = fibonacci_recursive(n)
  print(m)

main()


# Arrays

arr = [10,20,30,40,50]
arr[1] = 21
for i in arr:
  print(i)

#Range of Array input
  
Input = int(input("Enter num: "))
Array = []
for i in range(0, Input):
  loop_input = int(input())
  Array.append(loop_input)
print(Array)


#2D ARRAY

reginal_country = [
  ["US", "CANADA"],
  ["INDIA", "UK"],
  ["GOA", "DEHLI"]
]

print(reginal_country[2][1])

# for i in reginal_country:
#   print(i[1])


#swap two number
def swap_two_num(a, b):
  temp = a
  a = b
  b = temp
  return a, b

print(swap_two_num(2,1))
'''
#Biggest of two interger

def biggest_of_two_num():
  a = int(input("enter a: "))
  b = int(input("enter b: "))

  if(a > b):
    print("A is biggest number")
  else:
    print("B is biggest number")  

print(biggest_of_two_num())    