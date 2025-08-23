class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for i, num in enumerate(citations):
            if n - i <= num:
                return n - i
        
        return 0
                
            

        