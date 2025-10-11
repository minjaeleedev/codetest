class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        digit = 0
        sums = []
        for n2 in reversed(num2):
            arr = deque(['0']*digit)
            carry = 0
            for n1 in reversed(num1):
                i1, i2 = int(n2), int(n1)
                mul = i1*i2 + carry
                carry = mul // 10
                arr.appendleft(str(mul%10))
            if carry != 0:
                arr.appendleft(str(carry))
            
            digit += 1
            sums.append(''.join(arr))
       
        res = sums[0]
        for s in sums[1:]:
            res = self.sum(res, s)

        return res
    
    def sum(self, s1:str, s2:str)->str:
        res = []
        large, small = (s1, s2) if len(s1) >= len(s2) else (s2, s1)
        diff = len(large) - len(small)
        carry = 0
        for i in range(len(small)-1, -1, -1):
            n1, n2 = large[i+diff], small[i]
            s = int(n1) + int(n2) + carry
            carry = 1 if s >= 10 else 0
            res.append(str(s % 10))
        
        idx = diff - 1
        while idx >= 0:
            r = int(large[idx]) + carry
            carry = 1 if r >= 10 else 0
            res.append(str(r % 10))
            idx -= 1
        
        if carry:
            res.append(str(carry))

        return ''.join(reversed(res))
        