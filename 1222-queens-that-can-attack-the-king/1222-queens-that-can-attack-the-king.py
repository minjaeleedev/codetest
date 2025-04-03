class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        kr, kc = king
        result = []
        store=set([f'{r}|{c}' for r, c in queens])
        for queen in queens:
            # same row
            qr, qc = queen
            if qr == kr:
                cc = qc
                while cc != kc:
                    cc += 1 if cc < kc else -1
                    if f'{qr}|{cc}' in store:
                        break
                
                if cc == kc:
                    result.append([qr, qc])
            
            # same col
            elif qc == kc:
                cr = qr
                while cr != kr:
                    cr += 1 if cr < kr else -1
                    if f'{cr}|{qc}' in store:
                        break
                
                if cr == kr:
                    result.append([qr, qc])
            
            # down diag
            elif kc - kr == qc - qr:
                cr, cc = qr, qc
                while cr != kr and cc != kc:
                    if cr < kr:
                        cr += 1
                        cc += 1
                    else:
                        cr -= 1
                        cc -= 1
                    if f'{cr}|{cc}' in store:
                        break
                
                if cr == kr:
                    result.append([qr, qc])
                
            # up diag
            elif kr+kc == qr + qc:
                cr, cc = qr, qc
                while cr != kr and cc != kc:
                    if cr < kr:
                        cr += 1
                        cc -= 1
                    else:
                        cr -= 1
                        cc += 1
                    if f'{cr}|{cc}' in store:
                        break
                
                if cr == kr:
                    result.append([qr, qc])
            
        return result