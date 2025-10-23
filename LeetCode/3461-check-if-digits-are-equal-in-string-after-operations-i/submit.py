class Solution:
    def hasSameDigits(self, s: str) -> bool:
        arr = list(map(int, s))
        while True:
            n = len(arr)
            if n == 2:
                break

            temp = []
            for i in range(n - 1):
                temp.append((arr[i] + arr[i + 1]) % 10)

            arr = temp

        return arr[0] == arr[1]
