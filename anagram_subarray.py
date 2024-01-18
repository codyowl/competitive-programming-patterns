'''
Given an array of strings, group anagrams together.
Anagrams : Two strings are anagrams if both have same characters and count of each character to be same.
In other words, they are shuffled version of one another.
Example – eat, tea, ate are anagrams
Input
Input= ["eat", "tea", "tan", "ate", "nat", "bat"]
Output
Output= [ ["ate", "eat","tea"], ["nat","tan"], ["bat"] ]
'''
def anagram_subarray(myarray):
    anagram_dict = dict()
    for data in myarray:
        anagram_dict[data] = [i for i in myarray if sorted(i) == sorted(data)]
    final_list = list()
    for key, value in anagram_dict.items():
        final_list.append(value)
    new_final_list = list()
    # removing duplicates from a list of list
    for data in final_list:
        if data not in new_final_list:
            new_final_list.append(data)
    print(new_final_list)        


myarray = ["eat", "tea", "tan", "ate", "nat", "bat"]    
anagram_subarray(myarray)       