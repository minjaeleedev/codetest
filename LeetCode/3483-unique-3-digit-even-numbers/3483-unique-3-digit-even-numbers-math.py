class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = {n:0 for n in range(10)}
        for digit in digits:
            freq[digit] += 1

        zero, even, total = 0, 0, 0
        for n in freq:
            if freq[n] > 0:
                if n == 0:
                    zero += 1
                if n % 2 == 0:
                    even += 1
                total += 1
        
        result = 0

        # all different : include 0XX
        result += even * (total-1) * (total-2)
        if zero == 1:
            # pattern 0XE
            result -= (even-1)*(total-2)

        # for 2 same and 1 different
        for k in freq:
            if freq[k] >= 2:
                if k == 0:
                    # pattern X00
                    result += total - 1
                elif k % 2 == 1:
                    # pattern OOE
                    result += even
                else:
                    # pattern EAE, EEA, AEE : distinct number is even
                    # subtract 0EE
                    result += 3 * (even - 1) - zero
                    # pattern OEE, EOE : distinct number is odd
                    result += 2 * (total-even)
            # for 3 same digit
            if freq[k] >= 3:
                if k > 0 and k % 2 == 0:
                    # pattern EEE
                    result += 1

        return result
