"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""
from collections import deque
class Solution:
    def findOrder(self, numCourses, prerequisites):
        # Step 1: Create a directed graph
        graph = [[] for _ in range(numCourses)]
        # Step 2: Add directed edges to the graph
        inDegrees = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            inDegrees[course] += 1
        # Step 3: Initialize queue with nodes with inDegree 0
        queue = deque([node for node in range(numCourses) if inDegrees[node] == 0])
        # Step 4: Perform topological sort
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in graph[node]:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    queue.append(neighbor)
        # Step 5: Check if all nodes are visited
        if len(result) == numCourses:
            return result
        else:
            return []


s = Solution()
print(s.findOrder(2, [[1,0]]))
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))