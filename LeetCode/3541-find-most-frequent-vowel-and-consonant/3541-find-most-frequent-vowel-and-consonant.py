class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = set('aeiou')
        counter = Counter(s)
        mx_vo = 0
        mx_con = 0
        for c, freq in counter.items():
            if c in vowel:
                if mx_vo < freq:
                    mx_vo = freq
            else:
                if mx_con < freq:
                    mx_con = freq

        return mx_vo + mx_con
            
