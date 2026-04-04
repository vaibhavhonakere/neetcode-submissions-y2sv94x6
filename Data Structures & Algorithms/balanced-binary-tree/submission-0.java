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
    boolean result = true;

    public boolean isBalanced(TreeNode root) {
        dfs(root);
        return this.result;
    }
    public int dfs(TreeNode node){
        if(node == null){
            return 0;
        }
        int depth_1 = dfs(node.left);
        int depth_2 = dfs(node.right);
        if(Math.abs(depth_1 - depth_2) > 1){
            this.result = false;
        }
        return Math.max(depth_1, depth_2) + 1;
    }
}
