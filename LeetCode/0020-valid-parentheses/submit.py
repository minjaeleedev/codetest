class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c == "[" or c == "(" or c == "{":
                st.append(c)
            elif c == "]":
                if not st or st[-1] != "[":
                    return False
                st.pop()
            elif c == "}":
                if not st or st[-1] != "{":
                    return False
                st.pop()
            elif c == ")":
                if not st or st[-1] != "(":
                    return False
                st.pop()

        return len(st) == 0
