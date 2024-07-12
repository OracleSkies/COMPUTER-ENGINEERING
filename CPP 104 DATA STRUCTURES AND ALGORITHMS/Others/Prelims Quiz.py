def evaluate(exp):
    stack = []
    for char in exp:
        if char.isdigit():
            stack.append(int(char))
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            if char == '+':
                stack.append(val2 + val1)
            elif char == '-':
                stack.append(val2 - val1)
            elif char == '*':
                stack.append(val2 * val1)
            elif char == '/':
                stack.append(val2 / val1)
    return stack.pop()
#print(evaluate("231*+8-"))

def sheesh():
    stack = []




