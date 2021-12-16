# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 5, 1.1

Problem statement: 

4. Modify your binary search algorithm (from #3) to work with words rather 
than integers.  Test it on a small list of words, e.g., 
["Monday",  "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]. 
The search should be case in-sensitive.

7. Now, test your binary search algorithm from #6 on a list of all 
English words in the dictionary. See this for a tip on how to get a list of 
all dictionary words. Note the time taken to search for a word. 
Compare it with your timing result from #5, and comment on your findings.

https://www.datasciencebytes.com/bytes/2014/11/03/get-a-list-of-all-english-words-in-python/ 
"""

#%% sequential search
def binary_search_word(list1, word):
    """
    Carry out a binary search of the given sorted list for a given word
    
    Parameters
    ----------
    list1: input list, sorted
    word: the value to be searched

    Returns
    -------
    True/False
    """

<YOUR-CODE-HERE>


#%% test binary search
mylist = ["Monday",  "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
assert (binary_search_word(mylist, "monDay")==True)
assert (binary_search_word(mylist, "Funday")==False)
print("Binary search test passed")


#%% testing sequential search on list of dictionary words

from nltk.corpus import words
word_list = words.words()
# prints 236736
print (len(word_list))

from timeit import default_timer as timer

list_of_words_to_search = ["yesterday", "omuamua", "waqar", "different", "obtuse", "zoo", "aardvark", "style", "zaazoozum", "aaaaaaaa"]

<YOUR-CODE-HERE>