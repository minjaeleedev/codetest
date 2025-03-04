class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        freq = Counter(nums)
        pairs = 0

        for string, frequency in freq.items():
            if target.startswith(string):
                # suffix of the current string
                suffix = target[len(string):]      
                pairs += frequency * freq[suffix]

                # Remove count of self pairs
                if string == suffix:
                    pairs -= freq[suffix]
        
        return pairs
