# Problem: 4107. Find Missing Elements
# Difficulty: Easy
# Language: Python3
# Link: https://leetcode.com/problems/find-missing-elements/

from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn = min(nums)
        mx = max(nums)

        seen = set(nums)
        ans = []

        for x in range(mn + 1, mx):
            if x not in seen:
                ans.append(x)

        return ans