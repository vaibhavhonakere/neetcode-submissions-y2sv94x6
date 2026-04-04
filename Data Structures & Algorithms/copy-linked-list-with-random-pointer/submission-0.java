/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        
        // Node ret = null;
        Node curr = head;
        HashMap<Node, Node> ret = new HashMap<>();
        ret.put(null, null);
        while(curr != null){
            ret.put(curr, new Node(curr.val));
            curr = curr.next;
        }
        curr = head;
        while(curr != null){
            Node copy = ret.get(curr);
            copy.next = ret.get(curr.next);
            copy.random = ret.get(curr.random);
            // ret.put(ret.get(curr.next).next, curr.next);
            // ret.put(ret.get(curr.random).next, curr.random);
            curr = curr.next;
        }
        // map[node].next = node.next;
        return ret.get(head);
        
    }
}
