#import relevant functions
import random
import json

#Create a list of vowels
vowels = 'a' or 'e' or 'i' or 'o' or 'u'

#Create function to count vowels
def num_vowels(string):
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    print(count)

#Test Function
num_vowels("Sara")
