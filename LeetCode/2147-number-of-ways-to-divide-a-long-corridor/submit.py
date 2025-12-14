class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = corridor.count("S")
        if seats == 0 or seats % 2 == 1:
            return 0

        if seats == 2:
            return 1

        seat_cnt = 0
        plant_cnt = 0
        result = 1
        MOD = 10**9 + 7
        for i in range(len(corridor)):
            cur = corridor[i]
            if cur == "S":
                if seat_cnt == 2:
                    result = result * (plant_cnt + 1) % MOD
                    seat_cnt = 0
                    plant_cnt = 0
                seat_cnt += 1
            else:
                if seat_cnt == 2:
                    plant_cnt += 1

        return result
