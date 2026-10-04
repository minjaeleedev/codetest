class Solution:
    def checkValidString(self, s: str) -> bool:
        st = []
        star_st = []
        for i, c in enumerate(s):
            if c == "(":
                st.append(i)
            elif c == "*":
                star_st.append(i)
            else:
                if st:
                    st.pop()
                elif star_st:
                    star_st.pop()
                else:
                    return False

        while star_st and st:
            if st.pop() > star_st.pop():
                return False

        return len(st) == 0
