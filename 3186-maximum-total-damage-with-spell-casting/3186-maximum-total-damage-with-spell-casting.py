class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        freq = Counter(power)
        keys = sorted(freq)
        dp = [0]*len(keys)
        for i in range(len(keys)):
            cur = keys[i]
            total_power = freq[cur] * cur
            prev_power = -1
            prev = i - 1
            for j in range(i-1, -1, -1):
                if keys[j] == cur - 1 or keys[j] == cur - 2:
                    continue
                
                prev_power = keys[j]
                prev = j
                break
            
            if prev_power != -1:
                total_power += dp[prev]
            
            dp[i] = max(dp[i-1], total_power)
        
        return dp[len(keys)-1]