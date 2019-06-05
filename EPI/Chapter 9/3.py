# bracket_matching

s='{)'
stack=[]
for i in s:
    if i=='{' or i=='[' or i=='(':
        stack.append(i)
    else:
        if i=='}' and stack[-1]== '{':
            stack.pop()
        if i==']' and stack[-1]== '[':
            stack.pop()
        if i==')' and stack[-1]== '(':
            stack.pop()
print(stack)
