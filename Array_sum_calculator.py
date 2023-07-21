class Arraysumcalculator:

    def __init__(self):
        self.array = []

    def take_input(self):
        n = int(input("enter the element: "))  

        i = 0
        while i < n:
            t = int(input())
            self.array.append(t)
            i+=1

    def calculate_sum(self):

        sum_of_array = 0
        i = 0
        while i < len(self.array):
            sum_of_array += self.array[i]
            i+=1
        return sum_of_array

L = Arraysumcalculator()            
L.take_input()
total = L.calculate_sum()
print("total sum of the array: ",total)

'''(using for loop)
lst = []

n = int(input("enter the numbers of elements: "))

for i in range(n):
    elements = int(input())
    lst.append(elements)

sm = 0
for em in lst:
    sm = sm + em  

print(sm)    
'''
