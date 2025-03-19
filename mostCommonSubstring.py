'''You are given a string of characters. Your task is to write a 
function that will find and return the most common substring of a 
given length in the input string. If two or more substrings have 
the same maximum frequency, you should return the lexicographically 
smallest one.

For example, given the input string "bananabananaba" and a substring 
length of 5, your function should return "anaba", since it appears 
twice and is lexicographically smaller than other substrings that 
also appear twice (e.g., "banan").

The expected time complexity for this task is 
O(str.length⋅length).'''

def find_most_common_substring(s: str, length: int) -> str:
    # TODO: implement the function
    if not s:
        return ''
    if len(s) <= length:
        return s
    subs = {}
    maxis = []
    for i in range(len(s)-length+1):
        print(s[i:length+i])
        if s[i:length+i] not in subs.keys():
            sub = s[i:length+i]
            subs[sub] = 1
        else:
            sub = s[i:length+i]
            subs[sub] += 1
    print(subs)
    max_val = max(subs.values())
    for key in subs:
        if subs[key] == max_val:
            maxis.append(key)
    maxis.sort()
    print(maxis)
    return "".join(maxis[0])
    
s = 'bananabananaba'
length = 5
print(find_most_common_substring(s, length))