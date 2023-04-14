

from functools import lru_cache
from typing import List
import math
import time
import resource 

# Approach 1: Dynamic Programming (Bottom-up: In-place)

# O(n^2) solution with O(n^2) space



class Solution1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(1, len(triangle)):
            for col in range(row + 1):
                smallest_above = math.inf
                if col > 0:
                    smallest_above = triangle[row - 1][col - 1]
                if col < row:
                    smallest_above = min(smallest_above, triangle[row - 1][col])
                triangle[row][col] += smallest_above
        return min(triangle[-1])
    
# Approach 2: Dynamic Programming (Bottom-up: Auxiliary Space)

# Time complexity O(n^2), Space comlexity O(n)

class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        prev_row = triangle[0]
        for row in range(1, len(triangle)):
            curr_row = []
            for col in range(row + 1):
                smallest_above = math.inf
                if col > 0:
                    smallest_above = prev_row[col - 1]
                if col < row:
                    smallest_above = min(smallest_above, prev_row[col])
                curr_row.append(triangle[row][col] + smallest_above)
            prev_row = curr_row
        return min(prev_row)
    
# Approach 3: Dynamic Programming (Bottom-up: Flip Triangle Upside Down)

# Time complexity O(n^2), Space comlexity O(n)

class Solution3:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        below_row = triangle[-1] 
        n = len(triangle)
        for row in reversed(range(n - 1)):       
            curr_row = []
            for col in range(row + 1):
                smallest_below = min(below_row[col], below_row[col + 1])
                curr_row.append(triangle[row][col] + smallest_below)
            below_row = curr_row
        return below_row[0]
    
# Approach 4: Memoization (Top-Down)

# O(n^2) solution with O(n^2) space

class Solution4:
    def minimumTotal(self, triangle):
        @lru_cache(maxsize=None)
        def min_path(row, col):
            path = triangle[row][col]
            if row < len(triangle) - 1:
                path += min(min_path(row + 1, col), min_path(row + 1, col + 1))
            return path
        return min_path(0, 0)

time_start = time.perf_counter()
#run your code
s  = Solution1()
print (s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
time_elapsed = (time.perf_counter() - time_start)  
memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
print ("%6.1f secs %5.1f MByte" % (time_elapsed,memMb))

time_start = time.perf_counter()

s  = Solution2()
print (s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
time_elapsed = (time.perf_counter() - time_start)  
memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
print ("%6.1f secs %5.1f MByte" % (time_elapsed,memMb))

time_start = time.perf_counter()

s  = Solution3()
print (s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
time_elapsed = (time.perf_counter() - time_start)  
memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
print ("%6.1f secs %5.1f MByte" % (time_elapsed,memMb))

time_start = time.perf_counter()

s  = Solution4()
print (s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
time_elapsed = (time.perf_counter() - time_start)  
memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
print ("%6.1f secs %5.1f MByte" % (time_elapsed,memMb))


    