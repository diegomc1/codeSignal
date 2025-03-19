'''You are given an array of n strings. 
Your task is to find the longest common 
suffix shared among all strings in the array. 
A suffix is a sequence of letters at the end of a word. 
For instance, in the word "flying," "ing" is a suffix.

If the given array is empty or there is no common suffix 
among the strings, your function should return an empty string.

For example, given an array of strings: 
["barking", "parking", "starking"], 
the longest common suffix is "arking".'''

def solution(strs):
    if not strs:
        return ""
    # Reverse all strings using a simple for loop
    rev = []
    result = []
    for s in strs:
        rev.append(s[::-1])
    min_str = min(rev, key=len)
    # TODO: Implement the function
    for i, val in enumerate(min_str):
        # print(min_str[i])
        for other in rev:
            # print(other[i])
            if other[i] != val:
                result = min_str[:i]
                return(result[::-1])
    return min_str[::-1]

print(solution(["barking", "parking", "starking"]))