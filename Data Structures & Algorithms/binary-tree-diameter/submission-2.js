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
    maxVal = 0
    diameterOfBinaryTree(root){
        this.maxDepth_1(root)
        return this.maxVal;
    }

    maxDepth_1(root) {
        if(!root){
            return 0
        }
        let left = this.maxDepth_1(root.left)
        let right = this.maxDepth_1(root.right)
        if(left || right){
            this.maxVal = Math.max(this.maxVal, left + right)
        }
        return Math.max(left, right) + 1
    }
}
