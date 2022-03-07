'''Celsius to Fahrenheit


You are making a Celsius to Fahrenheit converter.
Write a function to take the Celsius value as an argument and return the corresponding Fahrenheit value.

Sample Input
36

Sample Output
96.8'''


celsius = int(input())

def conv(c):
    c = 9/5 * celsius + 32
    return c

fahrenheit = conv(celsius)
print(fahrenheit)

#The following equation is used to calculate the Fahrenheit value: 9/5 * celsius + 32