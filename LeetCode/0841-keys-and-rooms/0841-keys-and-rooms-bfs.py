class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = [False] * len(rooms)
        q = deque([0])
        visit[0] = True
        while q:
            idx = q.popleft()
            key_list = rooms[idx]
            for key in key_list:
                if not visit[key]:
                    visit[key] = True
                    q.append(key)                    
        
        for v in visit:
            if not v:
                return False
        
        return True