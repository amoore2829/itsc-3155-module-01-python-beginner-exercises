#Take in an integer greater than 1. 
#Print out the cubes of each integer from 0 to the inputted integer.


number_cube = int(input('Enter an integer greater than 1: '))
for i in range (0, number_cube+1):
    print(f'The cube of  {i} is {i*i*i}')
