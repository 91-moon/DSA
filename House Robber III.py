# Leetcode : https://leetcode.com/problems/house-robber-iii/
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def recursion(root):
            rob, not_rob = 0, 0
            if not root:
                return 0, 0
            lrob, lnot_rob = recursion(root.left)
            rrob, rnot_rob = recursion(root.right)

            rob = root.val + lnot_rob + rnot_rob
            not_rob = max(lrob, lnot_rob) + max(rrob, rnot_rob)
            return rob, not_rob

        return max(recursion(root))




