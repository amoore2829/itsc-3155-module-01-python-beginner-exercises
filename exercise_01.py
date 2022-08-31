#Write a script that takes in a grade from 0-100 inclusive 
#(include both 0 and 100 in the range). Assuming a normal 10 point grading scale, print off whether the user got an A, B, C, D, or F.


number_grade = int(input('Enter a grade from 0 to 100: '))

if number_grade >= 90:
    print('You got an A')
elif int(number_grade) >= 80:
    print('You got a B')
elif int(number_grade) >= 70:
    print('You got a C')
elif int(number_grade) >= 60:
    print('You got a D')
else:
    print('You got an F')

    