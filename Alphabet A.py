for row in range(7):
    for col in range(5):
        if col in {1,2,3} and row ==0:
            print('*', end=' ')
        elif row!=0 and col in {0,4}:
            print('*', end=' ')
        elif row==3:
            print('*',end= ' ')
        else:
            print(' ',end=' ')
    print()
