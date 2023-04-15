'''
Given a string s, return the length of the longest 
substring
 that contains at most two distinct characters.

 

Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
 

Constraints:

1 <= s.length <= 105
s consists of English letters.
'''

class Solution:

    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        if not s:
            return 0
        left = 0
        right = 0   
        max_len = 0
        char_map = {}
        while right < len(s):
            char_map[s[right]] = right
            right += 1
            if len(char_map) > 2:
                left = min(char_map.values())
                del char_map[s[left]]
                left += 1
            max_len = max(max_len, right - left)

        return max_len
    
s = Solution()
print(s.lengthOfLongestSubstringTwoDistinct("eceba"))
print(s.lengthOfLongestSubstringTwoDistinct("ccaabbb"))
