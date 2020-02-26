for row in range(7):
    for col in range(5):
        if row == 0 :
            print('*',end= ' ')
        elif col == 2 and row!=6:
            print('*',end=' ')
        elif row==5 and col ==0:
            print('*',end=' ')
        elif col==1 and row== 6:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()