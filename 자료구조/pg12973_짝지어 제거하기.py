def solution(s):
    answer = 0
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        answer = 1
    else:
        answer = 0

    return answer