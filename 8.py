n = int(input("enter the number of rows: "))
for i in range(n):
    print('* '*(i+1))
for i in range(n-1):
    print("* "* (n-i-1))
