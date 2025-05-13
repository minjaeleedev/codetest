class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counter = sorted([item for item in Counter(s).items()], key=lambda x:x[1])
        if len(counter) < k:
            return 0
        
        return sum([v for k,v in counter[:len(counter)-k]])