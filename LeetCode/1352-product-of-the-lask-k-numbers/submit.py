class ProductOfNumbers:
    def __init__(self):
        self.pref = [1]
        self.zi = -1
        self.cnt = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.zi = self.cnt
            self.pref = [1]
            self.cnt += 1
            return

        self.pref.append(num * self.pref[-1])
        self.cnt += 1

    def getProduct(self, k: int) -> int:
        if self.cnt - self.zi <= k:
            return 0

        return self.pref[-1] // self.pref[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
