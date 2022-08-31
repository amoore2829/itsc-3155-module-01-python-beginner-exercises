#Take in 10 integers from user. Create a new list with only elements which appear once. 
#Print both lists.


lst1 = []
unique_list = []

for x in range (10):
    num = int(input(f'Enter number {x+1}: '))
    lst1.append(num)

for x in range(10):
    if lst1.count(lst1[x]) == 1:
        unique_list.append(lst1[x])

print ('Original List: ', lst1)
print ('Nums that appear once: ', unique_list)

#Worked with Bishal, Emre, and Sudamsh