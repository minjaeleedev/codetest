class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        alpha = set('abcdefghijklmnopqrstuvwxyz')
        for a in alpha:
            if counter[a]:
                counter[a] -= 1
                v = [counter[x] for x in alpha if x in counter and counter[x]]
                if len(v) == 0 or min(v) == max(v):
                    return True
                counter[a] += 1
        return False
