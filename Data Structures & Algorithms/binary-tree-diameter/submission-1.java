/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    private int maxDepth;
    public int diameterOfBinaryTree(TreeNode root) {
        this.maxDepth = -1;
        dfs(root);
        return this.maxDepth;
    }
    private int dfs(TreeNode root){
        if(root == null){
            return 0;
        }
        int left = dfs(root.left);
        int right = dfs(root.right);
        if(left + right > this.maxDepth){
            this.maxDepth = left + right;
        }
        return 1 + Math.max(left, right);
    }
}
