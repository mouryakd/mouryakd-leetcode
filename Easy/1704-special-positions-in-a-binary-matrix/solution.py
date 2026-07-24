# Problem: 1704. Special Positions in a Binary Matrix
# Difficulty: Easy
# Language: Python3
# Link: https://leetcode.com/problems/special-positions-in-a-binary-matrix/

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        row_count = [0] * m
        col_count = [0] * n

        # Count 1s in each row and column
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        ans = 0

        # Count special positions
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    ans += 1

        return ans