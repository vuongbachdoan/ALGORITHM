# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        self.traversal(root)

    def traversal(self, node):
        if node.left:
            self.traversal(self, node.left)
        else:
            print(node.val)
            return node.val
        if node.right:
            self.traversal(self, node.right)
        else:
            print(node.val)
            return node.val
        