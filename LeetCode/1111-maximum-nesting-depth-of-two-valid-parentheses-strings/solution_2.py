from typing import List


class Solution:
    """
    Approach 2: Find the Pattern

    - For an opening parenthesis (, the parity of the index is opposite to the parity of the nesting depth:
        - An opening parenthesis at an odd index has an even nesting depth (assigned to group 0).
        - An opening parenthesis at an even index has an odd nesting depth (assigned to group 1).
    - For a closing parenthesis ), the parity of the index is the same as the parity of the nesting depth:
        - A closing parenthesis at an odd index has an odd nesting depth (assigned to group 1).
        - A closing parenthesis at an even index has an even nesting depth (assigned to group 0).
    """

    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = list()
        for i, ch in enumerate(seq):
            if ch == "(":
                ans.append(i % 2)
            else:
                ans.append(1 - i % 2)
            # The above code can also be abbreviated to
            # ans.append((i & 1) ^ (ch == '('))
            # C++ and JavaScript code provide direct shorthand methods.
        return ans
