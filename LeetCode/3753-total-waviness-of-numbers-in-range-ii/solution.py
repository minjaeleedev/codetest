from functools import lru_cache


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        """
        Approach 1: Digit Dynamic Programming
        Time Complexity: O(D^3 log num_2)
        Space Complexity: O(D^2 log num_2)
        """

        #  calculate the sum of the volatility values of all numbers in the range [0, num]
        def solve(num: int) -> int:
            # if the number is less than 3, the fluctuation value is 0
            if num < 100:
                return 0
            s = str(num)
            n = len(s)

            @lru_cache(None)
            def dfs(pos: int, prev: int, curr: int, isLimit: bool, isLeading: bool):
                # end position
                if pos == n:
                    return 1, 0

                # calculate the number of filling schemes and the fluctuation value under current conditions
                cnt = 0
                waviness = 0
                up = int(s[pos]) if isLimit else 9
                for digit in range(up + 1):
                    newLeading = isLeading and (digit == 0)
                    # the previous number is updated to curr
                    newPrev = curr
                    # the current number is updated to digit
                    newCurr = -1 if newLeading else digit
                    subCnt, subSum = dfs(
                        pos + 1,
                        newPrev,
                        newCurr,
                        isLimit and (digit == up),
                        newLeading,
                    )
                    # only calculate the volatility value when there are no leading zeros
                    if not newLeading and prev >= 0 and curr >= 0:
                        # when the value is a peak or a trough, update the current fluctuation value
                        if (prev < curr and curr > digit) or (
                            prev > curr and curr < digit
                        ):
                            waviness += subCnt

                    cnt += subCnt
                    waviness += subSum

                return cnt, waviness

            _, totalSum = dfs(0, -1, -1, True, True)
            return totalSum

        return solve(num2) - solve(num1 - 1)
