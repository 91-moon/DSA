#Leetcode : 1110. Delete Nodes And Return Forest
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        to_delete = set(to_delete)

        def dfs(node, is_root):

            if not node:
                return node
            deleted = True if node.val in to_delete else False

            if node.val not in to_delete and is_root:
                result.append(node)

            node.left = dfs(node.left, deleted)
            node.right = dfs(node.right, deleted)
            return None if deleted else node

        result = []
        dfs(root, True)
        return result