# Problem: 3812. Smallest Palindromic Rearrangement I
# Difficulty: Medium
# Language: Python3
# Link: https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)

        left = []
        middle = ""

        for ch in sorted(freq):
            left.append(ch * (freq[ch] // 2))
            if freq[ch] % 2:
                middle = ch

        left = "".join(left)
        right = left[::-1]

        return left + middle + right