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
     * @return {number}
     */
    count = 0
    dfs(root, maxVal){
        if(!root){
            return null
        }
        if(root.val >= maxVal){
            maxVal = root.val
            this.count += 1
        }
        this.dfs(root.left, maxVal)
        this.dfs(root.right, maxVal)
    }
    goodNodes(root) {
        this.dfs(root, root.val)
        return this.count
    }
}
