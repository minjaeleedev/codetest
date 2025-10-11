class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, result = 0, 0
        c_set = set()
        for right in range(len(s)):
            c = s[right]
            while c in c_set:
                c_set.remove(s[left])
                left += 1

            c_set.add(c)
            result = max(result, right - left + 1)
            
        return result