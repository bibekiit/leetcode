"""
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

 

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
"""

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        max_diff = 0
        for i in range(1, len(nums)):
            max_diff = max(max_diff, nums[i] - nums[i-1])
        return max_diff
    
# Time Complexity: O(nlogn)
# Space Complexity: O(1)

# Solution 2: Bucket Sort
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        max_num, min_num = max(nums), min(nums)
        
        bucket_size = max(1, (max_num - min_num) // (len(nums) - 1))
        bucket_num = (max_num - min_num) // bucket_size + 1
        buckets = [[] for _ in range(bucket_num)]
        for num in nums:
            buckets[(num - min_num) // bucket_size].append(num)
        max_diff = 0
        prev_max = min_num
        for bucket in buckets:
            if not bucket:
                continue
            max_diff = max(max_diff, bucket[0] - prev_max)
            prev_max = bucket[-1]
        return max_diff
    
# Time Complexity: O(n)
# Space Complexity: O(n)

# Solution 3: Radix Sort
#
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        max_num = max(nums)
        exp = 1
        while max_num // exp > 0:
            buckets = [[] for _ in range(10)]
            for num in nums:
                buckets[num // exp % 10].append(num)
            nums = []
            for bucket in buckets:
                nums.extend(bucket)
            exp *= 10
        max_diff = 0
        for i in range(1, len(nums)):
            max_diff = max(max_diff, nums[i] - nums[i-1])
        return max_diff
    
s = Solution()
print(s.maximumGap([100,3,2,1]))
