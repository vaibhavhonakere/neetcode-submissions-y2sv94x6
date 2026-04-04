// class Node {
//   constructor(val, next = null, random = null) {
//       this.val = val;
//       this.next = next;
//       this.random = random;
//   }
// }

class Solution {
    /**
     * @param {Node} head
     * @return {Node}
     */
    copyRandomList(head) {
        const cache = new Map();
        cache.set(null, null);
        let curr = head;
        while(curr){
            cache.set(curr, new Node(curr.val))
            curr = curr.next
        }
        curr = head;
        while(curr){
            const copy = cache.get(curr);
            copy.next = cache.get(curr.next)
            copy.random = cache.get(curr.random)
            curr = curr.next
        }
        return cache.get(head)

    }
}
