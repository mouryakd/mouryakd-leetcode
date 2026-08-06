# Problem: 3626. Smallest Divisible Digit Product I
# Difficulty: Easy
# Language: Python3
# Link: https://leetcode.com/problems/smallest-divisible-digit-product-i/

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product = 1
            for digit in str(n):
                product *= int(digit)

            if product % t == 0:
                return n

            n += 1