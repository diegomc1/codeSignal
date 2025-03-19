'''
Your task is to create a recursive function
reverse_string(s) that reverses a given string
s using recursion without using Python's built-in
functions like reversed() or [::-1].

For example, reverse_string("hello") would
return "olleh".'''


def reverse_string(s, index = -1, revString = ''):
    # TODO: implement the function to reverse the string using recursion.
    if index > -len(s) -1:
        revString += s[index]
        index -= 1
        return reverse_string(s, index, revString)
    else:
        return revString
print(reverse_string('hello'))