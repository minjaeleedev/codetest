class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        space_idx = 0
        temp = []
        for i, c in enumerate(s):
            if space_idx < len(spaces) and spaces[space_idx] == i:
                temp.append(" ")
                space_idx += 1
            
            temp.append(c)
        
        return ''.join(temp)
                
            
            