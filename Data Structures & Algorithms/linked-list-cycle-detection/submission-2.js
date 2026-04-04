/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {boolean}
     */
    hasCycle(head) {
        let first = head
        let second = head.next
        while(second && second.next){
            first = first.next
            second = second.next.next
            if(first == second){
                return true
            }
        }
        return false
    }
}
