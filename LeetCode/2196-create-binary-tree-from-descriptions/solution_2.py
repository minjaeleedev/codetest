from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Approach 2: Convert to Graph with Depth First Search
    """

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # Step 1: Organize data
        parent_to_children = {}
        all_nodes = set()
        children = set()

        for parent, child, is_left in descriptions:
            # Store child information under parent node
            if parent not in parent_to_children:
                parent_to_children[parent] = []
            parent_to_children[parent].append((child, is_left))
            all_nodes.add(parent)
            all_nodes.add(child)
            children.add(child)

        # Step 2: Find the root
        root_val = (all_nodes - children).pop()

        # Step 3 & 4: Build the tree using DFS
        def _dfs(val):
            # Create new TreeNode for current value
            node = TreeNode(val)

            # If current node has children, recursively build them
            if val in parent_to_children:
                for child, is_left in parent_to_children[val]:
                    # Attach child node based on is_left flag
                    if is_left:
                        node.left = _dfs(child)
                    else:
                        node.right = _dfs(child)
            return node

        return _dfs(root_val)
