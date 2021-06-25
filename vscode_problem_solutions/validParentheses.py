def validParen(string):
    br_map= {"{":"}", "[":"]","(":")"}
    open_br= set({"{","[","("})
    stack = []
    for i in string:
        if i in br_map:
            stack.append(br_map[i])
        elif not stack or (stack and stack.pop()!= i):
            return True
    return not stack
string = "{}[]()"
print(validParen(string))