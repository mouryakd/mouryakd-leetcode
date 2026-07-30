# Problem: 3275. Minimum Number of Pushes to Type Word I
# Difficulty: Easy
# Language: Python3
# Link: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        
        for i in range(len(word)):
            ans += (i // 8) + 1
            
        return ans