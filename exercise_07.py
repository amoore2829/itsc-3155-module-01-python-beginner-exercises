#Take in integers until the user types "QUIT" and store the numbers in a list. 
#Assume any input other than "QUIT" is a valid integer. Create another list of just the even numbers and print both lists.

lst1 = []
lst2 = []

user_quit = True


while user_quit:
    num = (input('Enter a number or QUIT to quit: '))
    if num == 'QUIT':
        break
    lst1.append(int (num))

for x in lst1:
    if (x % 2 == 0):
        lst2.append(x)
    
print ('Original List: ', lst1)
print ('Nums that appear once: ', lst2)

#Worked with Bishal, Emre, and Sudamsh