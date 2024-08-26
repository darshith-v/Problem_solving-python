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

'''
