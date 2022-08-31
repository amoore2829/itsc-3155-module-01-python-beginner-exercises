#Write a script that takes in two strings from the user. If one string is the suffix of the other string, print "True", otherwise, print "False". For example, if the user enters "brush" and "paintbrush", then the script would print "True". If the user entered "painting" and "painted", the script would print "False" because no string ends with the other. Keep in mind that the the pair "brush" and "paintbrush" as well as the pair "paintbrush" and "brush" 
#would print "True" because order does not matter.

x= input("Enter a string: ")
y= input("Enter another string: ")

if y[-len(x):] == x:
    print(True)
else:
    print(False)
