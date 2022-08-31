#Take in a string from the user and split it into an array of single characters. 
#Split the list of characters into a list of lists where each inner list has 3 elements. 
#Notice that the last inner array may have less than 3 elements.

lst1 = []

word = input('Enter a string: ')
word_length = len(word)
start = 0
end = 3
for index_word in range(start, word_length, end):

    added_words = word[index_word:index_word+3]
    words_count = list(added_words)
    lst1.append(words_count)

print(lst1)

#Worked with Bishal, Emre, and Sudamsh