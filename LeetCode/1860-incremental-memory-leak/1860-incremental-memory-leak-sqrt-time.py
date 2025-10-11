class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        # 2^31 - 1 -2 - 3... O(min(m1,m2))
        # 8 11
        # 8 11-1
        # 8 11-1-2
        # 8-3 11-1-2
        # 8-3 11-1-2-4
        # 8-3-5 11-1-2-4
        # 6 - break
        t = 1
        while True:
            if memory1 >= memory2:
                if memory1 >= t:
                    memory1 -= t
                else:
                    break
            else:
                if memory2 >= t:
                    memory2 -= t
                else:
                    break
            
            t += 1
        
        return [t, memory1, memory2]