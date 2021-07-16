"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

    -1: The number I picked is lower than your guess (i.e. pick < num).
    1: The number I picked is higher than your guess (i.e. pick > num).
    0: The number I picked is equal to your guess (i.e. pick == num).

Return the number that I picked.



Example 1:

Input: n = 10, pick = 6
Output: 6

"""
PICK = 6


def guess(n: int) -> int:
    if n < PICK:
        return 1
    elif n > PICK:
        return -1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            pivot = left + (right - left) // 2
            res = guess(pivot)
            if res == 1:
                left = pivot + 1
            elif res == -1:
                right = pivot - 1
            else:
                break
        return pivot


assert Solution().guessNumber(10) == 6
