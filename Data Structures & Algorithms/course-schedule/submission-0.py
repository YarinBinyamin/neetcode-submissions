class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        not_visit = set()
        for i in range(numCourses):
            not_visit.add(i)
        
        adjancey_list = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for edge in prerequisites: # [a,b] : b->a
            a,b = edge
            indegree[a] +=1
            adjancey_list[b].append(a)
        
        qeueu = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                qeueu.append(i) # all the starting points
        while qeueu:
            cur_course = qeueu.pop()
            not_visit.remove(cur_course)
            for c in adjancey_list[cur_course]:
                indegree[c] -=1
                if indegree[c] == 0 :
                    qeueu.append(c)
        if len(not_visit) == 0:
            return True
        return False