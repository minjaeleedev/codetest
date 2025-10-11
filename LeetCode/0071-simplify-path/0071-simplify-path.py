class Solution:
    def simplifyPath(self, path: str) -> str:
        st =[]
        for c in path.split('/'):
            if not c:
                continue
            
            if c == '.':
                continue
            
            if c == '..':
                if st:
                    st.pop()
                continue 
                
            st.append(c)
        
        return '/'+'/'.join(st)

            
                