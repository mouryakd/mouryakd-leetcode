# Problem: 3859. Maximum Product of Two Digits
# Difficulty: Easy
# Language: Python3
# Link: https://leetcode.com/problems/maximum-product-of-two-digits/

class Solution:
    def maxProduct(self, n: int) -> int:
        first = -1
        second = -1

        while n > 0:
            d = n % 10

            if d >= first:
                second = first
                first = d
            elif d > second:
                second = d

            n //= 10

        return first * second