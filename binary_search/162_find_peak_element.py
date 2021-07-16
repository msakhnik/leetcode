"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.



Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            pivot = left + (right - left) // 2
            if nums[pivot] > nums[pivot + 1]:
                right = pivot
            else:
                left = pivot + 1
        return left


assert Solution().findPeakElement([1, 2, 3, 1]) == 2
assert Solution().findPeakElement([1,2,1,3,5,6,4]) == 5
