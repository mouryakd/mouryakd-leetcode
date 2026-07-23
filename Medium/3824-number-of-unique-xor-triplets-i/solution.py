# Problem: 3824. Number of Unique XOR Triplets I
# Difficulty: Medium
# Language: Python3
# Link: https://leetcode.com/problems/number-of-unique-xor-triplets-i/

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1
        if n == 2:
            return 2

        return 1 << n.bit_length()