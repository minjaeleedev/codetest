class Solution:
    def decodeString(self, s: str) -> str:
        def is_digit(s:str):
            digit = set('0123456789')
            for c in s:
                if not c in digit:
                    return False
            return True
        
        st = []
        cur_digit = ''
        for c in s:
            if c == '[':
                if cur_digit:
                    st.append(cur_digit)
                    cur_digit = ''
            elif c == ']':
                last = deque([])
                while st and not is_digit(st[-1]):
                    last.appendleft(st.pop())
                
                if st and is_digit(st[-1]):
                    multiple = int(st.pop())
                    st.append(multiple * ''.join(last))
            elif is_digit(c):
                cur_digit = cur_digit + c
            else:
                st.append(c)
        
        return ''.join(st)