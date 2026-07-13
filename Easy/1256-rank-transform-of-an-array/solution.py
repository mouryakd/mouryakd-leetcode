# Problem: 1256. Rank Transform of an Array
# Difficulty: Easy
# Language: Python3
# Link: https://leetcode.com/problems/rank-transform-of-an-array/

class Solution:
    def arrayRankTransform(self, arr):
        sorted_unique = sorted(set(arr))
        rank_map = {value: rank + 1 for rank, value in enumerate(sorted_unique)}
        return [rank_map[num] for num in arr]