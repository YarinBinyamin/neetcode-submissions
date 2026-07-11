class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        index = 0
        while index < len(s):
            if s[index] == ']':
                cur_s =""
                while stack[-1] !='[':
                    cur_s = stack.pop() + cur_s
                stack.pop()
                num_str = ""
                while stack and stack[-1].isdigit():
                    num_str = stack.pop() + num_str
                num = int(num_str)
                stack.append(num * cur_s)
            else:
                stack.append(s[index])
            index+=1
        return "".join(stack)        
    