class Solution:
    def checkValidString(self, s: str) -> bool:
            stack1 = []
            stack2 = []
            n = len(s)
            index = 0
            while index < n :
                c = s[index]
                if c == '*':
                    stack2.append(index)
                elif c == '(':
                    stack1.append(index) 
                elif c ==')':
                    if stack1 and s[stack1[-1]] == '(':
                        stack1.pop()
                    elif stack2 and s[stack2[-1]] == '*':
                        stack2.pop()
                    else: 
                        return False       
                index +=1
                
            if not stack1:
                return True
            if stack1 and not stack2:
                return False
            if stack1 and stack2:
                for i in range(len(stack1)):
                    if not stack2:
                        return False
                    a = stack1.pop()
                    b  = stack2.pop()
                    if not (a < b):
                        return False
            return True