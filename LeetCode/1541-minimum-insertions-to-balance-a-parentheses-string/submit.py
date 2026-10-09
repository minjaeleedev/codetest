class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        st = []
        for c in s:
            if c == "(":
                if st and st[-1] == 1:
                    res += 1
                    st.pop()

                st.append(2)
            else:
                if not st:
                    res += 1
                    st.append(2)
                    st[-1] -= 1
                elif st[-1] == 1:
                    st.pop()
                else:
                    st[-1] -= 1

        return res + sum(st)
