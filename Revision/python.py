'''
def solveMefirst(a,b):
  return a + b;

num1 =  int(input())
num2 = int(input())
res = solveMefirst(num1,num2)
print(res)

def simpleArraySum(arr):
  return sum(arr)


myArray = [1,2,3,4,5];
print(simpleArraySum(myArray));


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
'''