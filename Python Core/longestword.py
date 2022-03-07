'''Longest Word


Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome
'''

text = input()

word = max(text.split(), key=len)
print(word)

#Recall the split(' ') method, which returns a list of words of the string.