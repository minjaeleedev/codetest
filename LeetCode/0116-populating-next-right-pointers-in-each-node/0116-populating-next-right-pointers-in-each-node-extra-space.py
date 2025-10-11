"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        by_lv = defaultdict(list)
        def traverse(root, lv):
            if not root:
                return None

            by_lv[lv].append(root)
            traverse(root.left, lv+1)
            traverse(root.right, lv+1)
        
        traverse(root, 0)
        for k in by_lv.keys():
            nodes = by_lv[k]
            for i in range(len(nodes)):
                if i == len(nodes) - 1:
                    nodes[i].next = None
                else:
                    nodes[i].next = nodes[i+1]
        
        return root
        