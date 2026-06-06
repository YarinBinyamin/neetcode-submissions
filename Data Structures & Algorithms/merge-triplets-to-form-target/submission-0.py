class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x,y,z = target
        ans = [False,False,False]
        for tri in triplets:
            if tri[0] == x:
                if y>=tri[1] and z >=tri[2]:
                    ans[0] = True
            if tri[1] == y:
                if x>=tri[0] and z >=tri[2]:
                    ans[1] = True     
            if tri[2] == z:
                if x>=tri[0] and y >=tri[1]:
                    ans[2] = True
        if ans[0] == True and ans[1] == True and ans[2] == True:
            return True
        return False