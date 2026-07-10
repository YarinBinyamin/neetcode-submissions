class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        index = 0 
        while index <len(asteroids):
            current = asteroids[index]
            alive = True
            
            while ans and ans[-1] > 0 and current < 0:
                if abs(current) > ans[-1]:
                    ans.pop()
                elif abs(current) < ans[-1]:
                    alive= False
                    break
                elif abs(current) == ans[-1]:
                    ans.pop()
                    alive= False
                    break

            if alive:
                ans.append(current)
            index+=1
        return ans