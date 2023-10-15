class Solution:

    def isAnagram(s: str, t: str) -> bool:
        
        # if the length of the strings are not equal, they are not anagrams
        if len(s) != len(t):
            return False

        # initialize two dictionaries to store the count of each character
        counter_s, counter_t = {}, {}

        # iterate through the strings and store the count of each character
        for char in s:
            counter_s[char] = 1 + counter_s.get(char, 0)
            
        # iterate through the strings and store the count of each character
        for char in t:
            counter_t[char] = 1 + counter_t.get(char, 0)

        # return True if the dictionaries are equal
        return counter_s == counter_t

