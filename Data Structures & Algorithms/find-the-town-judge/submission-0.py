class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
            incoming = {}
            outcoming = {}
            for e in trust:
                incoming[e[1]] = incoming.get(e[1],0) +1  # how many turst e[1]
                outcoming[e[0]] = outcoming.get(e[0],0) +1 # how manny e[0] trust

            for i in range(1,n+1):
                if incoming.get(i, 0) == n - 1 and i not in outcoming:
                    return i
            return -1
                