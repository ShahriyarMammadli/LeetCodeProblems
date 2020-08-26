# Shahriyar Mammadli
# LeetCode problem '20. Valid Parentheses' solution
# Import required libraries

def validParantheses(string):
    # Solving the problem using stack
    # Return True if the input set is empty
    if len(string) < 1:
        return True
    stack = []
    for i in string:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        elif i == ')' and len(stack) > 0 and stack.pop() == '(':
            continue
        elif i == ']' and len(stack) > 0 and stack.pop() == '[':
            continue
        elif i == '}' and len(stack) > 0 and stack.pop() == '{':
            continue
        else:
            return False
    return True if len(stack) == 0 else False

print("[[]]")