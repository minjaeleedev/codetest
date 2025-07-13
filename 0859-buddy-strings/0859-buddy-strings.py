class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        len_s, len_goal = len(s), len(goal)
        if len_s != len_goal:
            return False
        
        if s == goal:
            return len(set(s)) < len(s)
        
        # assert : two strings are different, and same length
        diff = []
        for i in range(len_s):
            if s[i] != goal[i]:
                diff.append(i)
        
        if len(diff) != 2:
            return False
        
        # assert : count of diff is two
        i, j = diff
        list_s = list(s)
        list_s[i], list_s[j] = list_s[j], list_s[i]
        
        return ''.join(list_s) == goal