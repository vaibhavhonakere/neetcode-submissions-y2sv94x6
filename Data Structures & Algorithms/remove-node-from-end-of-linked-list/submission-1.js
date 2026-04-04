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
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head, n) {
        const dummy = new ListNode(0, head)
        let curr = dummy;
        let move = head;
        while(n > 0){
            move = move.next;
            n--;
        }
        while(move){
            curr = curr.next
            move = move.next
        }
        curr.next = curr.next.next
        return dummy.next

    }
}
