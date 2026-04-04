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
     * @param {ListNode} l1
     * @param {ListNode} l2
     * @return {ListNode}
     */
    addTwoNumbers(l1, l2) {
        // const dummy = new ListNode();
        // let curr = dummy;
        // let carry = 0;
        // while(l1 | l2 | carry){
        //     const v1 = l1 ? l1.val : 0;
        //     const v2 = l2 ? l2.val : 0;
        //     const sum = v1 + v2
        // }
        let carry = 0
        let ret = new ListNode(0)
        let dummy = ret;
        let first = l1;
        let second = l2;

        // while(l1){
        //     let temp = l1.next
        //     l1.next = first
        //     first = l1
        //     l1 = temp
        // }
        // while(l2){
        //     let temp = l2.next
        //     l2.next = second
        //     second = l2
        //     l2 = temp
        // }

        while(first && second){
            let sum = first.val + second.val + carry;
            let quotient = sum % 10;
            let rem = Math.floor(sum / 10);
            carry = rem;
            dummy.next = new ListNode(quotient);
            dummy = dummy.next
            first = first.next;
            second = second.next;
        }
        while(first){
            dummy.next = new ListNode((first.val + carry) % 10)
            dummy = dummy.next
            carry = Math.floor((first.val + carry) / 10);
            first = first.next
        }
        while(second){
            dummy.next = new ListNode((second.val + carry) % 10)
            dummy = dummy.next
            carry = Math.floor((second.val + carry) / 10);
            second = second.next
        }
        if(carry){
            dummy.next = new ListNode(carry)
            dummy = dummy.next
        }
        return ret.next;

    }
}
