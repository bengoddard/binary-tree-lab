from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    left_height = max_depth(root.left)
    right_height = max_depth(root.right)

    return max(left_height, right_height) + 1

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    current_val = root.val
    if p.val < current_val and q.val < current_val:
        return lowest_common_ancestor(root.left, p, q)
    if p.val > current_val and q.val > current_val:
        return lowest_common_ancestor(root.right, p, q)
    return root