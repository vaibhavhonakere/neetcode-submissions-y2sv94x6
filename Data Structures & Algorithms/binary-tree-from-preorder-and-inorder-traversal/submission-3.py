# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = TreeNode(None)
        curr = head
        i, j, n = 0, 0, len(preorder)
        while i < n and j < n:
            # Go right and then as far left as possible
            curr.right = TreeNode(preorder[i], right = curr.right)
            curr = curr.right
            i += 1
            while i < n and curr.val != inorder[j]:
                curr.left = TreeNode(preorder[i], right=curr)
                curr = curr.left
                i += 1
            j += 1
            while curr.right and j < n and curr.right.val == inorder[j]:
                prev = curr.right
                curr.right = None
                curr = prev
                j += 1

        return head.right

        
        # if not preorder or not inorder:
        #     return None

        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        # return root
        # def dfs(preorder, inorder):
        #     if(not(preorder) or not(inorder)):
        #         return None
            
        #     root = TreeNode(preorder[0])
        #     index = inorder.index(preorder[0])
        #     root.left = dfs(preorder[1: index + 1], inorder[:index])
        #     root.right = dfs(preorder[index + 1:], inorder[index + 1:])
        #     return root
        
        # return dfs(preorder, inorder)