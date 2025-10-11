class Solution:
    def concatHex36(self, n: int) -> str:
        def convert(num:int, base:int):
            result = []
            while num:
                result += chr(num%base+ord('0')) if num%base < 10 else chr(num%base+ord('A')-10)
                num //= base
            
            return ''.join(reversed(result))

        d = convert(n**2, 16)
        t = convert(n**3, 36)

        return d+t
        