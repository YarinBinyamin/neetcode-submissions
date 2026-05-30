class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans= [0] * len(temperatures)
        index = 0
        while index < len(temperatures):
            if not stack or temperatures[stack[-1]]> temperatures[index]:
                stack.append(index)
            else:
                while stack and temperatures[stack[-1]] < temperatures[index]:
                    cur = stack.pop()
                    ans[cur] = index - cur 
                stack.append(index)
            index+=1
        return ans