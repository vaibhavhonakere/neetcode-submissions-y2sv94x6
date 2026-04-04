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
    public int goodNodesNum = 0;
    public int goodNodes(TreeNode root) {
        dfs(root, root.val);
        return goodNodesNum;
    }
    public void dfs(TreeNode node, int newMax){
        if(node == null){
            return;
        }
        if(node.val >= newMax){
            newMax = node.val;
            goodNodesNum += 1;
        }
        dfs(node.left, newMax);
        dfs(node.right, newMax);
        return;
    }
}
