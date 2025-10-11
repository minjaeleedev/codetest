class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # add guess's idx.
        bulls = set()
        cows = set()
        digit_idx_map = defaultdict(set)
        digit_counter = defaultdict(int)
        for i, c in enumerate(secret):
            digit_idx_map[c].add(i)
        
        # count bulls first
        for i, c in enumerate(guess):
            if not c in digit_idx_map:
                continue
            
            if i in digit_idx_map[c]:
                bulls.add(i)
                digit_counter[c] += 1
        
        for i, c in enumerate(guess):
            if not c in digit_idx_map:
                continue

            if len(digit_idx_map[c]) > digit_counter[c]:
                if i not in bulls and i not in cows:
                    cows.add(i)
                    digit_counter[c] += 1
        
        return str(len(bulls)) + 'A' + str(len(cows)) + 'B'