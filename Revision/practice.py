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

'''
# Find the perfect number between 1 to 100;

count = 0

for i in range(1,100):
  for j in range(1,i):
    if (i % j == 0):
      count += j
  if(count==i):
    print(count)
  count = 0    




