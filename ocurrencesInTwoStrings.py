'''You are given two strings, string1 and string2. 
Your goal is to determine a new string, string3, 
that is formed by characters that occur in both string1 
and string2 in the same order as they occur in string1.

Characters in string3 should maintain their original 
sequence order from string1. If a character is repeated 
in string1 and string2, include that character in string3 
as many times as it occurs in both strings, 
but not more than that.

For example, given string1 = "apple" and string2 = "peach", 
the resulting string3 would be "ape".

Your algorithm should not exceed a time complexity of 
O(string1.length+string2.length).'''

def solution(string1, string2):
    # TODO: Implement the function here
    str1 = {}
    str2 = {}
    arr = ''
    counter = 1
    for i in string2:
        if i not in str2.keys():
            str2[i] = 1
        else:
            counter += 1
            str2[i] = counter
    for i in string1:
        if i in str2.keys():
            if str2[i] > 0:
                arr += i
                str2[i]=str2[i]-1
        
    print(arr)

solution("apppple", "peach")