'''
Sum of Consecutive Numbers


No one likes homework, but your math teacher has given you an assignment to find the sum of the first N numbers.

Let’s save some time by creating a program to do the calculation for you!

Take a number N as input and output the sum of all numbers from 1 to N (including N).

Sample Input
100

Sample Output
5050

'''

N = int(input())
#your code goes here
sum = 0

for i in range(1, N+1):
    sum += i

print(sum)

#Explanation: The sum of all numbers from 1 to 100 is equal to 5050.