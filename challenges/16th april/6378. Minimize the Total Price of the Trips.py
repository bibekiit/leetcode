"""
There exists an undirected and unrooted tree with n nodes indexed from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Each node has an associated price. You are given an integer array price, where price[i] is the price of the ith node.

The price sum of a given path is the sum of the prices of all nodes lying on that path.

Additionally, you are given a 2D integer array trips, where trips[i] = [starti, endi] indicates that you start the ith trip from the node starti and travel to the node endi by any path you like.

Before performing your first trip, you can choose some non-adjacent nodes and halve the prices.

Return the minimum total price sum to perform all the given trips.

 

Example 1:


Input: n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]]
Output: 23
Explanation: The diagram above denotes the tree after rooting it at node 2. The first part shows the initial tree and the second part shows the tree after choosing nodes 0, 2, and 3, and making their price half.
For the 1st trip, we choose path [0,1,3]. The price sum of that path is 1 + 2 + 3 = 6.
For the 2nd trip, we choose path [2,1]. The price sum of that path is 2 + 5 = 7.
For the 3rd trip, we choose path [2,1,3]. The price sum of that path is 5 + 2 + 3 = 10.
The total price sum of all trips is 6 + 7 + 10 = 23.
It can be proven, that 23 is the minimum answer that we can achieve.
Example 2:


Input: n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]]
Output: 1
Explanation: The diagram above denotes the tree after rooting it at node 0. The first part shows the initial tree and the second part shows the tree after choosing node 0, and making its price half.
For the 1st trip, we choose path [0]. The price sum of that path is 1.
The total price sum of all trips is 1. It can be proven, that 1 is the minimum answer that we can achieve.
 

Constraints:

1 <= n <= 50
edges.length == n - 1
0 <= ai, bi <= n - 1
edges represents a valid tree.
price.length == n
price[i] is an even integer.
1 <= price[i] <= 1000
1 <= trips.length <= 100
0 <= starti, endi <= n - 1
"""
from collections import deque
from typing import List

class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        path = [[] for _ in range(n)]
        for u, v in edges:
            path[u].append(v)
            path[v].append(u)
        parent = [-1] * n
        depth = [0] * n
        stack = [(-1, 0)]
        tree = [[] for _ in range(n)]
        while stack:
            p, u = stack.pop()
            for v in path[u]:
                if v != p:
                    tree[u].append(v)
                    parent[v] = u
                    stack.append((u, v))
                    depth[v] = depth[u] + 1
        weight = [0] * n
        for u, v in trips:
            if depth[u] > depth[v]:
                u, v = v, u
            while depth[u] != depth[v]:
                weight[v] += 1
                v = parent[v]
            while u != v:
                weight[u] += 1
                weight[v] += 1
                u = parent[u]
                v = parent[v]
            weight[u] += 1

        def dfs(u):
            tmp0, tmp1 = 0, weight[u] * price[u] // 2
            for v in tree[u]:
                x0, x1 = dfs(v)
                tmp0 += max(x0, x1)
                tmp1 += x0
            return tmp0, tmp1
        res0, res1 = dfs(0)
        tot = sum(x * y for x, y in zip(price, weight))
        return tot - max(res0, res1)

s = Solution()
print (s.minimumTotalPrice(4, [[0,1],[1,2],[1,3]], [2,2,10,6], [[0,3],[2,1],[2,3]]))
print (s.minimumTotalPrice(2, [[0,1]], [2,2], [[0,0]]))
