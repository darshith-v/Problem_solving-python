def reverse_array(lt,start,end):
    i = start
    j = end
    while i<j:
        t = lt[i]
        lt[i] = lt[j]
        lt[j] = t

        i+=1
        j-=1
    return lt


arr = []
n = int(input("enter n: "))
print("enter the element one by one")

for i in range(0,n):
    arr.append(int(input()))    

k = int(input("enter the rotation start from: "))
def rotate_array(lt,k):
    n = len(lt)

    #so the array is divided into 2 part, as first is 
    p1 = reverse_array(lt,0,n-k-1)

    #second part is 
    p2 = reverse_array(lt,n-k,n-1)

    #finally total the both p1 and p2 
    p3 = reverse_array(lt,0,n-1)

    return p3 

result = rotate_array(arr,k)
print(result)
