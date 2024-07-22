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

count = 0
for i in range(1,100):
  for j in range(1,i):
    if (i % j == 0):
      count += j
  if(count==i):
    print(count)
  count = 0    



# python file

from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello world"

app.run(host='0.0.0.0',port=5000)    


# Dockerfile

FROM python

WORKDIR /src/
COPY app.py/src/

RUN pip install flask

ENTRYPOINT ["Python", "app.py"]



# In Terminal

1. docker ps

2. docker image build -t myhello .

3. docker container run -p 9000:5000 myhello

4. docker image tag myhello darshithv3392/myhello

5. docker image push darshithv3392/myhello

6. kubectl run dars --image=darshithv3392/myhello --port=9000 --labels app=demo

7. kubectl port -forward pod/dars 9000:5000

8. kubectl get pods --selector app=demo

'''


