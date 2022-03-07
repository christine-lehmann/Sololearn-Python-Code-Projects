'''
FizzBuzz

FizzBuzz is a well known programming assignment, asked during interviews.

The given code solves the FizzBuzz problem and uses the words "Solo" and "Learn" instead of "Fizz" and "Buzz".
It takes an input n and outputs the numbers from 1 to n.
For each multiple of 3, print "Solo" instead of the number.
For each multiple of 5, prints "Learn" instead of the number.
For numbers which are multiples of both 3 and 5, output "SoloLearn".

You need to change the code to skip the even numbers, so that the logic only applies to odd numbers in the range.

'''

N = int(input())

for i in range(1, N, 2):
    if i % 3 == 0 and i % 5 == 0:
        print("Sololearn") 
    elif i % 3 == 0:
        print("Solo")
    elif i % 5 == 0:
        print("Learn")
    else:
        print(i)
#Remember, the continue statement can be used to skip a loop iteration.