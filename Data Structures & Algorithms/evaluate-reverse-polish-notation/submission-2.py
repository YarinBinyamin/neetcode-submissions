class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result =0 
        index =0 
        while index < len(tokens):
            c = tokens[index]
            if c == '+' or c =='-' or c == '/' or c =='*':
                last = int(stack.pop())
                first = int(stack.pop())
                if c == '+':   
                    stack.append(first + last)
                if c == '-':   
                    stack.append(first - last)
                if c == '*':   
                    stack.append(first * last)
                if c == '/':   
                    stack.append(int(first / last))
            else:
                stack.append(c)
            index+=1
        return int(stack.pop())