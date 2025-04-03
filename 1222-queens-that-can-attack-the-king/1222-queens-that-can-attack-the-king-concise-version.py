class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        kr, kc = king
        result = []
        store={(i,j) for i, j in queens}
        for i in [-1,0,1]:
            for j in [-1, 0 ,1]:
                for k in range(1,8):
                    x, y = kr + i * k, kc + j * k
                    if (x, y) in store:
                        result.append([x,y])
                        break
        
        return result

