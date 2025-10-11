"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        # hash_map : key is old Node, value is new Node.
        hash_map = {}
        
        cur = head
        while cur:
            hash_map[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            hash_map[cur].next = hash_map.get(cur.next)
            hash_map[cur].random = hash_map.get(cur.random)
            cur = cur.next
        
        return hash_map[head]
            
