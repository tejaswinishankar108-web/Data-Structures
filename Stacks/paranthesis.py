def isValid(s: str) -> bool:
    stack =[]
    balance = True
    index = 0
    while index < len(s) and balance:
        if s[index] == '(' or s[index] == '[' or s[index] == '{':
            stack.append(s[index])
        else:
            if len(stack) == 0:
                balance = False
            else:
                top = stack.pop()
                if s[index] == ')' and top != '(':
                    balance = False
                if s[index] == ']' and top != '[':
                    balance = False
                if s[index] == '}' and top != '{':
                    balance = False
        index += 1
    if balance and len(stack) == 0:
        return True
    else:
        return False
print(isValid("({[}])"))