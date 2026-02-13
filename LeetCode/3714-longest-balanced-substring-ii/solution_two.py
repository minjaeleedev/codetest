class Solution:
    def longestBalanced(self, s: str) -> int:
        def balanced_a(s, a: str):
            count = 0
            max_run = 0
            for char in s:
                if char == a:
                    count += 1
                    if count > max_run:
                        max_run = count
                else:
                    count = 0
            return max_run

        def balanced_ab(s, a: str, b: str, _: str):
            diff = 0
            last = {0: 0}
            max_len = 0
            for i, char in enumerate(s, 1):
                if char == a:
                    diff += 1
                elif char == b:
                    diff -= 1
                else:
                    diff = 0
                    last.clear()
                if diff in last:
                    cur_len = i - last.get(diff)
                    if max_len < cur_len:
                        max_len = cur_len
                else:
                    last[diff] = i

            return max_len

        def balanced_abc(s: str):
            diff_ab, diff_ac = 0, 0
            last = {(0, 0): 0}
            max_len = 0
            for i, char in enumerate(s, 1):
                if char == "a":
                    diff_ab += 1
                    diff_ac += 1
                elif char == "b":
                    diff_ab -= 1
                else:
                    diff_ac -= 1

                if (diff_ab, diff_ac) in last:
                    cur_len = i - last.get((diff_ab, diff_ac))
                    if max_len < cur_len:
                        max_len = cur_len
                else:
                    last[(diff_ab, diff_ac)] = i

            return max_len

        return max(
            balanced_a(s, "a"),
            balanced_a(s, "b"),
            balanced_a(s, "c"),
            balanced_ab(s, "a", "b", "c"),
            balanced_ab(s, "a", "c", "b"),
            balanced_ab(s, "b", "c", "a"),
            balanced_abc(s),
        )
