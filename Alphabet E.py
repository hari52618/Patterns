for row in range(7):
    for col in range(5):
        if row in {0,3,6} :
            print('*',end=' ')
        elif col==0:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()