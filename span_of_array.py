# # span of array

# n = int(input("enter the no. of element: "))
# lt = []

# for i in range(n):
#     lt.append(int(input()))

# mx = lt[0]    
# mn = lt[0]

# for em in lt:
#     if lt[i] > mx:
#         mx = lt[i]
#     if lt[i] < mn:
#         mn = lt[i]   

# total = mx - mn
# print(total)        
 
 #or 

lt = []
n = int(input("enter the no of elements: "))

for i in range(n):
    lt.append(int(input()))

max_of_array = max(lt)    
min_of_array = min(lt)

total = max_of_array - min_of_array
print(total)