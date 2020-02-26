for row in range(7):
    for col in range(5):
        if col==0:
            print('*', end=' ')
        elif row in {0,3,6} and col!=4:
            print('*', end=' ')
        elif col==4 and row!=0 and row!=3 and row!=6:
            print('*', end=' ')
        else:
            print(' ',end=' ')
    print()
