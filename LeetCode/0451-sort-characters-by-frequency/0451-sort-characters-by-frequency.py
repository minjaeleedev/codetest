class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1
        
        freq = sorted(cnt.items(), key=lambda x:-x[1])
        result = ''
        for f in freq:
            result += f[0]*f[1]

        return result