class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i = 1
        s = set()
        while i * i <= n:
            if n % i == 0:
                s.add(i)
                s.add(n//i)
            i+=1
        
        arr = sorted(list(s))
        return -1 if len(arr) < k else arr[k-1]
