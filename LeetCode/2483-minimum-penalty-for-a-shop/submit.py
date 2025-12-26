# three pass. not efficient
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        penalties = [0] * (n + 1)
        for i in range(n):
            if customers[i] == "Y":
                penalties[0] += 1

        for i in range(1, n + 1):
            penalties[i] = penalties[i - 1]
            if penalties[i] == 0:
                continue

            if customers[i - 1] == "Y":
                penalties[i] -= 1
            else:
                penalties[i] += 1

        mn = min(penalties)
        res = -1
        for i in range(n + 1):
            if penalties[i] == mn:
                res = i
                break

        return res
