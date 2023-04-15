"""
Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.
 

Example 1:

Input
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
Output
[null, null, null, null, true, false]

Explanation
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, return true
twoSum.find(7);  // No two integers sum up to 7, return false
 

Constraints:

-105 <= number <= 105
-231 <= value <= 231 - 1
At most 104 calls will be made to add and find.
"""

class TwoSum:
    
    def __init__(self):

        self.nums = []

    def add(self, number: int) -> None:

        self.nums.append(number)

    def find(self, value: int) -> bool:

        nums = self.nums

        for i in range(len(nums)):

            for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] == value:

                    return True

        return False
    

# Complexity Analysis
# 
# Time Complexity: O(n^2), where n is the number of elements in the data structure.
#
# Space Complexity: O(n), where n is the number of elements in the data structure.  

# Complexity can be improved by using a hash table to store the number of occurrences of each number in the data structure.

import collections

class TwoSum:

    def __init__(self):

        self.nums = collections.Counter()

    def add(self, number: int) -> None:

        self.nums[number] += 1

    def find(self, value: int) -> bool:

        for num in self.nums:

            if value - num in self.nums:

                # 

                if value - num != num or self.nums[num] > 1:

                    return True

        return False

