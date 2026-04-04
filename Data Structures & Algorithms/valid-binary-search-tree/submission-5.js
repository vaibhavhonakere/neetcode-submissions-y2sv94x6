/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {boolean}
     */
    dfs(leftMin, root, rightMax){
        if(!root){
            return true
        }
        if(!(leftMin < root.val && root.val < rightMax)){
            return false
        }
        return this.dfs(leftMin, root.left, root.val) && this.dfs(root.val, root.right, rightMax) 
    }
    isValidBST(root) {
        return this.dfs(-10001, root, 10001)
    }
}
