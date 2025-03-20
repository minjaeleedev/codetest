class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        wait = 0
        cur = customers[0][0]
        for arrival, duration in customers:
            if arrival > cur:
                cur = arrival
            cur += duration
            wait += cur - arrival

        return wait / n