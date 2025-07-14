class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        inc = arr[0] < arr[1]
        if not inc:
            return False
        
        for i in range(len(arr)-1):
            cur, nxt = arr[i], arr[i+1]
            if inc:
                if cur > nxt:
                    inc = False
                elif cur == nxt:
                    return False
            else:
                if cur <= nxt:
                    return False
        
        return not inc