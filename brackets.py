def check_brackets(s):

    if len(s) == 1:
        return False

    d = {'(': ')', '[': ']', '{': '}'}
    d1 = {'(': 1, ')': 1, '[': 1, ']': 1, '{': 1, '}': 1}

    index = []
    strs = ''

    for i in range(len(s)):
        if s[i] in d1:
            strs += s[i]
            index.append(i)

    stack = []
    stack_index = []

    for i in range(len(strs)):
        if strs[i] in d:
            stack.append(strs[i])
            stack_index.append(i)
        else:
            if stack == []:
                return False
            top = stack.pop()
            stack_index.pop()
            if strs[i] != d[top]:
                return False
    if stack_index != []:
        return False

    return True


if __name__ == '__main__':
    str_in = str(input())
    print(check_brackets(str_in))
