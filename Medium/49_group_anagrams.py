import collections
def groupAnagrams(list : list[str]):
    
    # initialize a dictionary to store the anagrams
    ans = collections.defaultdict(list)
    
    # iterate through the list of strings
    for s in strs:
        count = [0] * 26
        # iterate through the characters in the string
        for c in s:
            count[ord(c) - ord("a")] += 1
        # append the string to the dictionary
        ans[tuple(count)].append(s)
    # return the values of the dictionary
    return ans.values()


