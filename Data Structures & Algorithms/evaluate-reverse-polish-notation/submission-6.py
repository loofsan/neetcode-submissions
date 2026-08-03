"""
We're going to use Stacks.
tokens = ["1","2","+","3","*","4","-"]

It will always be valid.
Expression = 'a'
Stack = [1, 2, ]

Helper Function:
def arithmetic(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    else:
        return a / b

Loop through the tokens:
    - if it is not part of the set of operations, 
        - we add it to the stack
    # (We know that it will always be a valid expression.)
    # That means that when the expression is not empty, we will 
    # always only need to .pop() one element before adding it to the expression.
    - if it is part of the operations:
    - if expression == 'a':
        - a = stack.pop()
        - b = stack.pop()
        - expression = arithmetic(a, b, current Element)
    - else:
        - a = stack.pop()
        - expression = arithmetic(expression, a, current Element)
    
    return expression


"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        
        return stack[0]