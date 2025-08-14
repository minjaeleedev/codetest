class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
            
        dna_map = {'A':1, 'C':2, 'T':3, 'G':4}
        rev_map = {'1':'A', '2':'C', '3':'T', '4':'G'}
        num_map = defaultdict(int)
        
        cur,digit = 0, 1
        for i in range(10):
            cur += dna_map[s[9-i]]*digit
            digit *= 10

        num_map[cur] += 1
        res = set()
        for i in range(10,len(s)):
            prev = dna_map[s[i-10]]
            l = dna_map[s[i-9]]
            r = dna_map[s[i]]
            
            cur -= prev * (10**9)
            cur *= 10
            cur += r
            if cur in num_map:
                seq = ''.join([rev_map[c] for c in str(cur)])
                res.add(seq)
            else:
                num_map[cur] += 1
        
        return list(res)

            
        