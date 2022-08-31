#Take in a number, n, from the user. Then, take in n floats from the user and store them in a list. 
#For instance, if the user enters 4, then the user will have to enter 4 numbers. Print the list and the mean.


n = int(input('Enter a number: '))
data = []
for i in range(0, n):
    ele = float(input('Enter a number: '))
    data.append(ele)

print('List: ', data)
print('Average: ', sum(data)/len(data))



#https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/