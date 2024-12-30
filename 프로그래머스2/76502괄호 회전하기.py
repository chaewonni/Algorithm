def solution(s):
    result = 0
    
    for i in range(len(s)):
        stack = []
        for j in range(i, i+len(s)):
            j = j % len(s)
            if s[j] == '{' or s[j] =='(' or s[j] == '[':
                stack.append(s[j])
            if s[j] == '}':
                if not stack:
                    break
                else:
                    if stack[-1] == '{':
                        stack.pop()
            if s[j] == ')':
                if not stack:
                    break
                else:
                    if stack[-1] == '(':
                        stack.pop()
            if s[j] == ']':
                if not stack:
                    break
                else:
                    print(stack[-1])
                    if stack[-1] == '[':
                        stack.pop()
        else:
            if not stack:
                result += 1
    
    
    return result