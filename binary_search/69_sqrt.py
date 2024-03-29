"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.

"""

from typing import List


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 2, x // 2
        while left <= right:
            pivot = left + (right - left) // 2
            power = pivot * pivot
            if power > x:
                right = pivot - 1
            elif power < x:
                left = pivot + 1
            else:
                return pivot
        return right


assert Solution().mySqrt(4) == 2
assert Solution().mySqrt(16) == 4
assert Solution().mySqrt(2147395599) == 46339
