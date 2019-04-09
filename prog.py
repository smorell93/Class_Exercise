import random

vowels = 'a' or 'e' or 'i' or 'o' or 'u'

def num_vowels(string):
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    print(count)

num_vowels("Sara")
