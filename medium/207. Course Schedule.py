"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""
from collections import deque
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list representation of the graph
        adj_list = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        
        # Populate the adjacency list and in-degree array
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1
        
        # Create a queue and add all the vertices with in-degree 0 to it
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # Keep track of the number of visited vertices
        visited = 0
        
        # Process the vertices in the queue
        while queue:
            vertex = queue.popleft()
            visited += 1
            
            # Decrement the in-degree of all the neighbors of the current vertex
            for neighbor in adj_list[vertex]:
                in_degree[neighbor] -= 1
                
                # If the neighbor has an in-degree of 0, add it to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If we have visited all the vertices, it is possible to finish all courses
        return visited == numCourses

    
s = Solution()

print(s.canFinish(2, [[1,0]]))

print(s.canFinish(2, [[1,0],[0,1]]))

print(s.canFinish(3, [[1,0],[1,2],[0,1]]))


