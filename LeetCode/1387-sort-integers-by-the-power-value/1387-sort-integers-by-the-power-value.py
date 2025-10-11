class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        cnt = defaultdict(int)
        for n in range(lo, hi+1):
            num = n
            cur = 0
            q = deque([])
            while num != 1:
                if num not in cnt:
                    q.append(num)
                if num % 2 == 0:
                    num = num // 2
                else:
                    num = 3 * num + 1
                
                cur += 1
            
            while q:
                cnt[q.popleft()] = cur
                cur -= 1
        
        result = []
        for n in range(lo, hi+1):
            result.append((n, cnt[n]))
            
        result.sort(key=lambda x:x[1])
        return result[k-1][0]