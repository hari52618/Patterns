n = int(input("enter the n value: "))
for i in range(n):
    print("  "*(n-i-1)+ '* ',end = '')
    if i >= 1:
        print('  '*(2*i-1)+'*',end='')
    print()