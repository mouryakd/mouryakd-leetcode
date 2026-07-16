# Problem: 190. Reverse Bits
# Difficulty: Easy
# Language: Python
# Link: https://leetcode.com/problems/reverse-bits/

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(32):
            # take the lowest bit of n and push it into result
            result = (result << 1) | (n & 1)
            n >>= 1
        return result