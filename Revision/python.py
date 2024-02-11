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

'''