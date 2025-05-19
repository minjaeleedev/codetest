class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        result = []
        for i in range(0, min(n-3,3)):
            for j in range(i+1, min(n-2, 6)):
                for k in range(j+1, min(n-1,9)):
                    arr = [s[:i+1], s[i+1:j+1], s[j+1:k+1], s[k+1:]]
                    is_valid = True
                    for a in arr:
                        if (len(a) != 1 and a[0] == '0') or int(a) > 255:
                            is_valid = False
                            break
                    
                    if not is_valid:
                        continue
                    
                    result.append('.'.join(arr))
        
        return result

