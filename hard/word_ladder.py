# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]

# Output: 5

# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.

# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]

# Output: 0

# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation.

# Constraints:

# 1 <= beginWord.length <= 100

# endWord.length == beginWord.length

# 1 <= wordList.length <= 5000

# wordList[i].length == beginWord.length

# beginWord, endWord, and wordList[i] consist of lowercase English letters.

# beginWord != endWord

# All the strings in wordList are unique.

# name 'List' is not defined
from typing import List
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        queue = collections.deque([(beginWord, 1)])
        print (list(queue))
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in wordList:
                        wordList.remove(new_word)
                        queue.append((new_word, length+1))
                        print (list(queue))
        return 0
    
# time complexity: O(n * m^2)
# space complexity: O(n * m^2)
    
s = Solution()
print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))
print(s.ladderLength("a", "c", ["a","b","c"]))

