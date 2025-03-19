'''Now, let's try to solve the same task more efficiently! 
We will still be searching for the longest common prefix 
in the given array of strings.

To add an additional layer of complexity, in this task, 
you need to find a more efficient approach with the 
expected complexity of 

O(strs.length⋅log(strs.length)⋅max_length).

Hint: think about ordering strings in some way.'''

def efficient_LCP(strs):
    # TODO: implement the solution here
    if not strs:
        return ''
    strs.sort()
    # Get the first and last strings in the sorted array
    first = strs[0]
    last = strs[-1]
    mini = min(len(first), len(last))
    # Find the common prefix between the first and last strings
    common_prefix = []
    for i in range(mini):
        if first[i] == last[i]:
            common_prefix.append(first[i])
        else:
            break
    return "".join(common_prefix)
strs = ["floss", "flight", "floral"]
print(efficient_LCP(strs))