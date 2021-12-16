# -*- coding: utf-8 -*-
"""
Practical Algorthns
Problem set: Unit 5, 1.1

Problem statement: 

4. Modify your sequential search algorithm (from #2) to work with words rather 
than integers.  Test it on a small list of words, e.g., 
["Monday",  "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]. 
The search should be case in-sensitive.

5. Now, test your sequential search algorithm from #4 on a list of all 
English words in the dictionary. See this for a tip on how to get a list 
of all dictionary words. Note the time taken to search for a word.

https://www.datasciencebytes.com/bytes/2014/11/03/get-a-list-of-all-english-words-in-python/

"""

#%% sequential search
def sequential_search_word(list1, word):
    """
    Carry out a sequential search of the given sorted list for a given word
    
    Parameters
    ----------
    list1: input list, sorted
    word: the word to be searched

    Returns
    -------
    True/False
    """

    for i in range(len(list1)):
        if list1[i].lower() > word.lower():
            return False        
        if list1[i].lower() == word.lower():
            return True
    return False

#%% test sequential_search
mylist = ["Monday",  "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
assert (sequential_search_word(mylist, "monDay")==True)
assert (sequential_search_word(mylist, "Funday")==False)
print("Sequential search test passed")


#%% testing sequential search on list of dictionary words

from nltk.corpus import words
word_list = words.words()
# prints 236736
print (len(word_list))

from timeit import default_timer as timer

list_of_words_to_search = ["yesterday", "omuamua", "waqar", "different", "obtuse", "zoo", "aardvark", "style", "zaazoozum", "aaaaaaaa"]

n = len(list_of_words_to_search)
results = {}
cumulative_time = 0

for word in list_of_words_to_search:
    start = timer()
    found = sequential_search_word(word_list, word)
    end = timer()
    time_taken = end-start
    results[word] = (round(time_taken,5), found)
    cumulative_time += time_taken
    
print("\n** Sequential Search of word list**")    
print("Search for these words: ", list_of_words_to_search)

print("\nTime taken to search various words and the result:")    
for k,v in results.items():
    print(k, v)

print("\nTotal time to carry out search of ", n, " words = ", round(cumulative_time,5), " seconds")
print("Average search time per word = ", round(cumulative_time/n,5), " seconds")



    
        
    
    








