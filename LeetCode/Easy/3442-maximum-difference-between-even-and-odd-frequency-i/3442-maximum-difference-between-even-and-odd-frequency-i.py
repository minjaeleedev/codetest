class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        odd = max([val for key, val in counter.items() if val % 2 == 1])
        even = min([val for key, val in counter.items() if val % 2 == 0])
        
        return odd - even