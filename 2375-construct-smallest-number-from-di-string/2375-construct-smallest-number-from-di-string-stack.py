class Solution:
    def smallestNumber(self, pattern: str) -> str:
        result = []
        st = []

        for i in range(len(pattern)):
            if pattern[i] == 'D':
                st.append(str(i+1))
            else:
                result.append(str(i+1))
                while st:
                    result.append(st.pop())
        
        last = str(len(pattern)+1)
        if pattern[-1] == 'D':
            st.append(last)
        else:
            result.append(last)
        
        while st:
            result.append(st.pop())
        
        return "".join(result)
