class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def wave(n: int) -> int:
            res = 0
            st = str(n)
            for i in range(1, len(st) - 1):
                if int(st[i - 1]) < int(st[i]) and int(st[i]) > int(st[i + 1]):
                    res += 1
                elif int(st[i - 1]) > int(st[i]) and int(st[i]) < int(st[i + 1]):
                    res += 1

            return res

        return sum([wave(n) for n in range(num1, num2 + 1)])
