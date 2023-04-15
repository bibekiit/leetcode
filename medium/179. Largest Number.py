"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
"""
from typing import List
class Solution:

    def largestNumber(self, nums: List[int]) -> str:

        nums = [str(num) for num in nums]

        nums.sort(key = lambda x: x * 10, reverse = True)

        return str(int(''.join(nums)))
    
s = Solution()
s.largestNumber([3,30,34,5,9])