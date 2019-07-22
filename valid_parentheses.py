class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        brackets = { '(': ')', '[':']','{': '}' }
        open_brackets = ('(','[','{')

        for brac in s:
            if brac in open_brackets:
                stack.append(brackets[brac])
            elif len(stack) != 0 and brac == stack[-1]:
                stack.pop()
            else:
                return False
        return True if len(stack) == 0 else False   
            
   
