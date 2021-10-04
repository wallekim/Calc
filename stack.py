def check_brackets(s):

    if len(s) == 1:
        return 1

    d = {'(':')', '[':']', '{':'}'}
    d1 = {'(': 1, ')': 1, '[': 1, ']': 1, '{': 1, '}': 1}

    index = []
    top = ''
    strs = ''

    for i in range(len(s)):
        if s[i] in d1:
            strs += s[i]
            index.append(i)


    stack = []

    for i in range(len(strs)):
        if strs[i] in d:
            stack.append(strs[i])
        else:
            if stack == []:
                return index[i]+1
            top = stack.pop()
            if strs[i] != d[top]:
                return index[i]+1

    if stack != []:
        return 1

    return 'Success'

s = str(input())

print(check_brackets(s))
