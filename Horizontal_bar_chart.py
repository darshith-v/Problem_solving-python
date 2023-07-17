#horizontal bar chart
def hor_bar_chart(new_lt,n):
    n = len(new_lt)
    for i in range(0,n):
        print(new_lt[i],end = '\t')
        for j in range(1,new_lt[i] + 1):
            print("*",end = '')    
        print()    


lt = []
n = int(input("enter the size of element: "))
print("enter the elements one by one")

for i in range(0,n):
    number = int(input("enter the elements: "))
    lt.append(number)

print(hor_bar_chart(lt,n))
