class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "]": "[", "}": "{"}

        if s[0] in brackets.keys():
            return False
        
        stack = []
        for c in s:
            if c in brackets.keys():
                if len(stack) == 0:
                    return False
                else:
                    if brackets[c] == stack[-1]:
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(c)
        print(stack)
        if len(stack) == 0:
            return True
        
        return False
