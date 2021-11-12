# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: 5.1 - Working with Data Structures

6a) Define a function which is given a string and returns a dictionary with words (strings) as keys and numbers as values,
showing how many times each word occurs in the original string. For example, when given the string:
"The first test of the function."
the function wordFreq() should return
{ "the":2, "first":1, "test":1, "of":1, "function":1 }

although of course the items might be in a different order. 

The function should ignore any non-letters in the string (so if the string contains "hello1 how are you", 
the 1 should be ignored), and convert everything to lower case. Test the function. 

The function split from the string module will be very useful for this exercise. 
It separates a string into blocks, using a given string to indicate where the blocks begin and end. For example,
"The first test of the function.".split(" ")
(argument is a space) returns
[ "The", "first", "test", "of", "the", "function." ]

Another hint: string.ascii_lowercase will return a string with all alphabets from a to z as a string.
And, you can check whether a particular chacter is in a string by using the "in" keyword. 
"""

import string

"""
ignore_non_letters_and_convert_to_lower(istring)

Input:
String - sentence with with words separate by whitespace

Returns:

A sanitized list of words in that string, 
where all upper case letters have been converted to lower case,
and all non-alphabets have been ignored
"""
def ignore_non_letters_and_convert_to_lower(istring):
    list_of_words = istring.split(" ")

    word_list_sanitized = []
    for i, word in enumerate(list_of_words):
        word = list_of_words[i].lower()
        newword = ""
        for c in word:
            if c in string.ascii_lowercase:
                newword += c
        word_list_sanitized.append(newword)
    return(word_list_sanitized)

"""
count_words(word_list)

Input: 
sanitized list of words

Returns:
dictionary with words as keys, and their counts as values
"""
def count_words(word_list):
    word_counts = {}
    for word in word_list:
        if word in word_counts.keys():
            word_counts[word]+=1
        else:
            word_counts[word]=1

    return(word_counts)


"""
wordFreq(istring):

Input:
String - sentence with with words separate by whitespace

Returns:
dictionary with words as keys, and their counts as values
"""
def wordFreq(istring):
    word_list_sanitized = ignore_non_letters_and_convert_to_lower(istring)
    word_counts = count_words(word_list_sanitized)
    return(word_counts) 


"""
#main
"""

mystring = "The first123 test of the Function. THE The T___HE the111"
word_counts = wordFreq(mystring)
print(word_counts)
