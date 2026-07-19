class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}  # 각 문자의 마지막 위치
        stack = []
        in_stack = set()

        for i, c in enumerate(s):
            if c in in_stack:
                continue
            # 스택 top이 c보다 크고, 뒤에 또 나온다면 → 지금 버리고 나중에 넣는 게 이득
            while stack and stack[-1] > c and last[stack[-1]] > i:
                in_stack.remove(stack.pop())

            stack.append(c)
            in_stack.add(c)

        return "".join(stack)
