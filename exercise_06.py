#Take in a row number from 1 to 5 inclusive and a column number from 1 to 5. Print out a grid of 0s, 
#but in the row and column entered by the user, print a 1.

row = int(input('Enter a row num from 1 to 5: '))
col = int(input('Enter a col num from 1 to 5: '))

for xrow in range(1, 6):
    for ycol in range(1, 6):
        if row == xrow and col == ycol:
            print('1', end= '')

        else:
            print('0', end= '')
    print('')

#worked with Bishal, Emre, and Sudhamsh           