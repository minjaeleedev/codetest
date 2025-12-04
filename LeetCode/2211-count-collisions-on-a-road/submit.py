class Solution:
    def countCollisions(self, directions: str) -> int:
        ls = list(directions)
        res = 0
        st = []
        first = True
        for i in range(len(ls)):
            c = ls[i]
            if c == "R":
                st.append(c)
                first = False
            elif c == "L":
                if not first:
                    res += 1

                while st:
                    res += 1
                    st.pop()
            elif c == "S":
                first = False
                while st:
                    res += 1
                    st.pop()

        return res
