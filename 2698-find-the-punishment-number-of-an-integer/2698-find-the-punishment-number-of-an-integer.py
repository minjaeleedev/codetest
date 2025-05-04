class Solution:
    def punishmentNumber(self, n: int) -> int:
        result = 0
        for i in range(1,n+1):
            sq = i*i
            if self.partition(sq, i):
                result += sq
        
        return result
    
    def partition(self, sq:int, target:int)->bool:
        str_sq = str(sq)
        temp = []
        def helper(sq, cur, idx):
            if idx == len(sq):
                return sum([int(num) for num in cur]) == target
            
            digit = sq[idx]
            f = helper(sq, cur+[digit], idx+1)
            last = cur[-1]
            s = helper(sq, cur[:-1]+[last+digit], idx+1)
            return f or s
        
        return helper(str_sq, [str_sq[0]], 1)

