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
     * @return {void}
     */
    reorderList(head) {
        let first = head;
        let second = head.next;
        while(second && second.next){
            first = first.next
            second = second.next.next
        }
        let save = first.next;
        first.next = null;

        let prev = null;
        while(save){
            let tmp = save.next;
            save.next = prev;
            prev = save;
            save = tmp;
        }
        while(prev){
            let tmp2 = head.next
            let tmp3 = prev.next
            head.next = prev
            prev.next = tmp2
            head = tmp2
            prev = tmp3
        }




    }
}
