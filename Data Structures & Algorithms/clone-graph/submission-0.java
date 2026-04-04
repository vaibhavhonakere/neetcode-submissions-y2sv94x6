/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        HashMap<Node,Node> old_to_New = new HashMap<>();
        return dfs(node, old_to_New);
        
    }
    private Node dfs(Node node, HashMap<Node,Node> old_to_New){
        if(node == null){
            return null;
        }
        if(old_to_New.containsKey(node)){
            return old_to_New.get(node);
        }
        Node copy = new Node(node.val);
        old_to_New.put(node,copy);
        for(Node nei: node.neighbors){
            copy.neighbors.add(dfs(nei, old_to_New));
        }
        return copy;
    }
}