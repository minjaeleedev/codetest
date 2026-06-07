from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # unique values -> use dict
        ht = defaultdict(dict)
        for parent, child, is_left in descriptions:
            if parent not in ht:
                ht[parent] = {"node": TreeNode(parent), "parent": parent}

            if child not in ht:
                ht[child] = {"node": TreeNode(child), "parent": parent}

            if is_left:
                ht[parent]["node"].left = ht[child]["node"]
            else:
                ht[parent]["node"].right = ht[child]["node"]

            ht[child]["parent"] = parent

        # find root
        root = None
        cur = descriptions[0][0]
        while not root or ht[cur]["parent"] != cur:
            root = ht[cur]["parent"]
            cur = root

        return ht[root]["node"]
