def vertical_bar_chart(lt1):
    n = len(lt1)    
    mx = lt1[0]
    for i in range(1,n):
        if lt1[i] > mx:
            mx = lt1[i]

    b = mx
    while b >= 1:
        for i in range(0,n):
            if lt1[i] >= b:
                print("* ",end = ' ')
            else:
                print("  ",end = ' ')
        print()        
        b-=1        

lt = []
n = int(input("enter the no of element: "))
print("enter the element one by one")

for i in range(0,n):
    lt.append(int(input("enter the element: ")))


result = vertical_bar_chart(lt)
print(result)