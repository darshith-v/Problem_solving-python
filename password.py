#password

def CheckPassword(s,n):              # s-sting and n is lenght(int) of string(c fuction pattern) 
    if n < 4:
        return 0
    if s[0].isdigit():
        return 0

    cap = 0
    num = 0
    for i in range(n):
        if s[i] == ' ' or s[i] == '/':
            return 0
        if s[i] >= 'A' and s[i] <= 'Z':            # capital alphabate words A - Z
            cap = cap + 1
        elif s[i].isdigit():                       # can have number
            num = num + 1

    if cap > 0 and num > 0:
        return 1
    else:
        return 0

#enter the Password
s = input("enter the password: ")            

#calculating length of string
a = len(s)

print(CheckPassword(s,a))