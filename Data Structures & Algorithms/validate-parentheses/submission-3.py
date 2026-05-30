class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] == '{' or s[i] == '[' or s[i] == '(' :
                stack.append(s[i])
            elif len(stack) != 0: 
                if (s[i] == '}' and stack[-1] == '{') or (s[i] == ')' and stack[-1] == '(') or (s[i] == ']' and stack[-1] == '[') :
                    stack.pop()
                else:
                    return False
            else:
                return False
        if len(stack) != 0:
            return False
        return True