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
     * @return {number[]}
     */
    rightSideView(root) {
        if(!root){
            return []
        }
        let queue = [root]
        let ret = []
        while(queue.length > 0){
            let lvl = []
            let length = queue.length;
            for(let i = 0; i < length; i++){
                let node = queue.shift();
                if(node.left){
                    queue.push(node.left)
                }if(node.right){
                    queue.push(node.right)
                }
                if(i == length - 1){
                    ret.push(node.val)
                }
            }
        }
        return ret
    }
}
