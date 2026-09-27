from collections import deque


class Solution:
    def reverseParentheses(self, s: str) -> str:
        i = 0
        st = []
        while i < len(s):
            if s[i] == "(":
                st.append(s[i])
            elif s[i] == ")":
                tmp = deque([])
                while st and st[-1] != "(":
                    tmp.append(st.pop())
                st.pop()
                while tmp:
                    st.append(tmp.popleft())
            else:
                st.append(s[i])

            i += 1

        return "".join(st)
