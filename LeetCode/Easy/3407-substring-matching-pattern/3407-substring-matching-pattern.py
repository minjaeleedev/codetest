class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        head, tail = p.split("*")
        i = 0
        is_match = False
        if head:
            while i < len(s)-len(head) - len(tail):
                if s[i:i+len(head)] == head:
                    is_match = True
                    break
                
                i += 1
        else:
            is_match = True
        
        if not is_match:
            return False
        
        if tail:
            j = len(s)
            tail_match = False
            while j >= i + len(head):
                if s[j-len(tail):j] == tail:
                    tail_match = True
                    break
                
                j -= 1
            if not tail_match:
                is_match = False
                 
        return is_match
            
            