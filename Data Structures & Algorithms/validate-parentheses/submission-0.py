class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack, push if we meet left parantheses, check against the top if we meet right, if good pop, otherwise return false
        stack=[]
        for c in s:
            if c in ['(','{','[']:
                stack.append(c)
            else:
                if not stack:
                    return False
                if c==')' and stack[-1]=='(' or c==']' and stack[-1]=='[' or c=='}' and stack[-1]=='{':
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False
                