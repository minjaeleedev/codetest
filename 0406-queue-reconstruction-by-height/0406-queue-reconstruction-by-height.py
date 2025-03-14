class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x:(-x[0], x[1]))
        result = deque([])
        for h, k in people:
            cnt = 0
            temp = []
            while cnt < k:
                cnt += 1
                if result:
                    temp.append(result.popleft())
            
            result.appendleft([h,k])
            while temp:
                result.appendleft(temp.pop())
            
        return list(result)
