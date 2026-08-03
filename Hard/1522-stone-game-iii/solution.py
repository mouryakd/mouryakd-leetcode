# Problem: 1522. Stone Game III
# Difficulty: Hard
# Language: Python3
# Link: https://leetcode.com/problems/stone-game-iii/

from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        # dp[i] = maximum score difference current player can achieve
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            dp[i] = float('-inf')
            total = 0

            for k in range(3):
                if i + k < n:
                    total += stoneValue[i + k]
                    dp[i] = max(dp[i], total - dp[i + k + 1])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"