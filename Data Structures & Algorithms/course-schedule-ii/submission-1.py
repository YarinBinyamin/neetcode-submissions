class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        
        not_visit = set()
        for i in range(numCourses):
            not_visit.add(i)
            
        adjency_list =  [[] for _ in range(numCourses)]
        
        indegree = [0] * numCourses
        for edge in prerequisites:
            indegree[edge[0]] += 1
            adjency_list[edge[1]].append(edge[0])  # edge[1] -> edge[0]
        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            course = queue.pop()
            ans.append(course)
            for c in adjency_list[course]:
                indegree[c] -=1
                if indegree[c] == 0:
                    queue.append(c)
        if len(ans) == numCourses :
            return ans
        else:
            return []