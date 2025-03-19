def solution(s):
    # TODO: implement the solution here
    result = []
    i = 0
    while i < len(s) - 1:
        result.append(s[i+1])
        result.append(s[i])
        i = i + 2
    if len(s) % 2 != 0:
        result.append(s[-1])
    swap = ''
    for char in result:
        swap += char
    print(swap)
        
solution('hello')