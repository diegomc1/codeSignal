'''
You are given a string s. Your task is to create a function 
that checks whether the string s consists of one repeated substring.

If it does, the function should return the substring. If there are 
multiple possible answers, return the longest one. If it does not 
consist of a repeated substring, return an empty string.

To clarify, a "repeated substring" refers to a pattern of characters 
that reoccurs throughout the full string, with no characters left over. 
For example, the string "abababab" consists of repeated substrings "ab" 
and "abab". On the other hand, the string "abcabcab" does not consist 
of a repeated substring, as the final characters "ab" do not complete 
the repeating pattern of "abc".'''

def repeat_substring(s):
    # TODO: implement the function according to the task requirements.
    if not s:
        return 0
    if len(s) == 1 :
        return ''
    div = round(len(s)//2)
    lens = len(s)
    times = 2
    for i in range(div, 0, -1):
        # print(s[:i], s[lens - i:], s[:i]*(lens//i))
        if s[:i] == s[lens - i:] and s[:i]*(lens//i) == s:
            # print(s[:i], s[lens - i:])
            return(s[:i])
        times+=1
    return ''
print(repeat_substring('lololololololololo'))