def greatest_id(l,n):
    n = len(l)
    mx = 0
    for i in range(1,n):
        if l[i] > l[mx]:
            mx = i
    return mx        

lt = []
n = int(input("enter n element: "))

for i in range(0,n):
    lt.append(int(input()))
print(lt)

def second_greatest(l,n):
    lgt = greatest_id(l,n)
    res = -1
    for i in range(0,n):
        if l[lgt] != l[i] :
            if res == -1 :
                res = i
            elif l[i] > l[res]:
                res = i
    return f"The second largest elements is {l[res]} and its index value is {res}  "

print(second_greatest(lt,n))

