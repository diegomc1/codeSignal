''' You are given a string s. Your task is to write a function that returns
a string in which every pair of adjacent characters in the original string is
swapped. If the string has an odd length, leave the last character as it is.

It is not allowed to use Python built-in functions like reverse() or join()
in this task, you should implement the solution without using them.

For example, if you are given the string "abcdef", your function should return
"badcfe". If the string is "hello", your function should return "ehllo".'''

def swap_adjacent(s):
    result = []  # Use a list to store the swapped characters

    i = 0
    while i < len(s) - 1:  # Loop through the string in pairs
        result.append(s[i + 1])  # Swap adjacent characters
        result.append(s[i])
        i += 2  # Move to the next pair

    if len(s) % 2 != 0:  # If the length is odd, add the last character
        result.append(s[-1])

    # Manually construct the final string
    swapped_string = ""
    for char in result:
        swapped_string += char
    
    return swapped_string

# **Example Usage**
print(swap_adjacent("abcdef"))  # Output: "badcfe"
print(swap_adjacent("hello"))   # Output: "ehllo"
print(swap_adjacent("abc"))     # Output: "bac"
print(swap_adjacent("a"))       # Output: "a"
print(swap_adjacent(""))        # Output: ""
