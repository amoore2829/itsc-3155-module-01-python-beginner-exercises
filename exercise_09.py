#Take in 5 words from the user and store them in a list.
#Then, create a single string from the individual words, separated by spaces, and print the list and resultant string.


lst = []
for x in range (5):
    words = input('Enter a word: ')
    lst.append(words)

print('words', lst)

print('One String: ', *lst, sep=' ')

#Worked with Bishal, Emre, and Sudamsh