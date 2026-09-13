# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if(not(root)):
            return TreeNode(val)
        
        curr = root
        prev = None
        while(curr):
            if(val > curr.val):
                if(not(curr.right)):
                    curr.right = TreeNode(val)
                curr = curr.right
            elif(val < curr.val):
                if(not(curr.left)):
                    curr.left = TreeNode(val)
                curr = curr.left
            else:
                break
        
        return root

