# Problem: 3276. Minimum Number of Pushes to Type Word II
# Difficulty: Medium
# Language: Python3
# Link: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)

        # Sort frequencies in descending order
        freq = sorted(freq.values(), reverse=True)

        ans = 0

        for i in range(len(freq)):
            ans += freq[i] * (i // 8 + 1)

        return ans