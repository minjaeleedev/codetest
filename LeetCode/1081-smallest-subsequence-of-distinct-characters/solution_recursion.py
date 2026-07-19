from collections import Counter


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        def solve(s: str):
            if not s:
                return ""  # base case: 빈 문제의 답

            cnt = Counter(s)
            pos = 0  # 첫 글자로 확정할 위치
            for i, c in enumerate(s):
                if c < s[pos]:
                    pos = i
                cnt[c] -= 1
                if cnt[c] == 0:
                    # c가 마지막 등장 → 더 미루면 c를 못 넣음
                    # 여기까지 본 것 중 최소인 pos에서 확정
                    break

            head = s[pos]
            # 확정한 문자를 제거한 나머지로 재귀
            rest = s[pos + 1 :].replace(head, "")
            return head + solve(rest)  # 자식이 부분문제의 정답을 준다고 믿고 조합

        return solve(s)
