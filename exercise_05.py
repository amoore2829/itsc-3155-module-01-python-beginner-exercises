#Take in 5 integers from the user and store them in a list. 
#Then take in another 5 integers and store them in a separate list. 
#Create a third array containing the common values from both arrays without duplicates. Print out all three lists.

lst1 = []
lst2 = []
common_list = []

for num in range (5):
    first_five = int(input('Enter a number for the first list: '))
    lst1.append(first_five)

for num in range (5):
    second_five = int(input('Enter a number for the second list: '))
    lst2.append(second_five)


common_list = set(lst1).intersection(lst2)

print ('First List: ', lst1)
print ('Second List: ', lst2)
print ('Common List: ', common_list)

#got help from https://java2blog.com/find-common-elements-in-two-lists-python/#:~:text=Using%20the%20intersection%20%28%29%20Function%20This%20is%20the,the%20elements%20which%20are%20common%20in%20two%20sets.


