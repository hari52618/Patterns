n = int(input("enter the no of rows: "))
for i in range(n):
    print('* '*(i+1)+'  '*(n-i-1),end= '')
    print()