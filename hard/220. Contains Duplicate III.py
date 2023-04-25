"""
You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:

i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.

 

Example 1:

Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0
Example 2:

Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.
 

Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
1 <= indexDiff <= nums.length
0 <= valueDiff <= 109
"""
from typing import List
# Solution 1: Brute Force
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if abs(i-j) <= indexDiff and abs(nums[i]-nums[j]) <= valueDiff:
                    return True
        return False
    
# Solution 2: Binary Search Tree
from sortedcontainers import SortedSet
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # Solution 2 - 64 ms
        if valueDiff < 0:

            return False

        tree = SortedSet()

        for i in range(len(nums)):
            if i > indexDiff:
                tree.remove(nums[i - indexDiff - 1])

            if tree.bisect_left(nums[i] - valueDiff) != tree.bisect_right(nums[i] + valueDiff):
                return True

            tree.add(nums[i])

        return False

# Solution 3: Bucket
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # Solution 3 - 64 ms
        if valueDiff < 0:
            return False
        buckets = {}
        for i, num in enumerate(nums):
            # bucket = num // (valueDiff + 1) is the key
            bucket = num // (valueDiff + 1)
            # bucket means the range of valueDiff
            # buckets contains the value of nums[i]
            if bucket in buckets:
                return True
            if bucket - 1 in buckets and abs(num - buckets[bucket - 1]) <= valueDiff:
                return True
            if bucket + 1 in buckets and abs(num - buckets[bucket + 1]) <= valueDiff:
                return True
            buckets[bucket] = num
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // (valueDiff + 1)]
        return False
