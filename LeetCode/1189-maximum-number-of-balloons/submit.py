from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        res = 0
        print(cnt)
        while (
            cnt["l"] >= 2
            and cnt["o"] >= 2
            and cnt["b"] >= 1
            and cnt["n"] >= 1
            and cnt["a"] >= 1
        ):
            cnt["b"] -= 1
            cnt["a"] -= 1
            cnt["l"] -= 2
            cnt["o"] -= 2
            cnt["n"] -= 1
            res += 1

        return res
