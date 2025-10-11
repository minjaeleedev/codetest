class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        idx = {n:i for i, n in enumerate(order)}
        
        friends.sort(key=lambda x:idx[x])
        return friends