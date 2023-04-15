# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
# 
#
# Example 1:
#
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
# Example 2:
#
# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
#
# Constraints:
#
# 1 <= points.length <= 300
# points[i].length == 2
# -104 <= xi, yi <= 104
# All the points are unique.
#
# Solution 1: Brute Force
#
# Time Complexity: O(n^3)
#
# Space Complexity: O(1)
#
# Solution 2: Hash Table
#
# Time Complexity: O(n^2)
#
# Space Complexity: O(n)
#
# Solution 3: Math
#
# Time Complexity: O(n^2)
#
# Space Complexity: O(1)
#
# Solution 4: Math + Hash Table
#
# Time Complexity: O(n^2)
#
# Space Complexity: O(n)
#
# Solution 5: Math + Hash Table
#
# Time Complexity: O(n^2)
#
# Space Complexity: O(n)
from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        max_points = 0
        for i in range(len(points)):
            same_points = 1
            slope_map = {}
            for j in range(i + 1, len(points)):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    same_points += 1
                else:
                    slope = self.get_slope(points[i], points[j])
                    if slope in slope_map:
                        slope_map[slope] += 1
                    else:
                        slope_map[slope] = 1
            max_points = max(max_points, same_points + max(slope_map.values(), default=0))
        return max_points
    
    def get_slope(self, point1, point2):
        if point1[0] == point2[0]:
            return float('inf')
        elif point1[1] == point2[1]:
            return 0
        else:
            return (point2[1] - point1[1]) / (point2[0] - point1[0])