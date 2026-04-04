/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Codec {

    private void dfsSerialize(TreeNode node, List<String> res){
        if(node == null){
            res.add("N");
            return;
        }
        res.add(Integer.toString(node.val));
        dfsSerialize(node.left, res);
        dfsSerialize(node.right, res);
        return;
    }

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        List<String> res = new ArrayList<>();
        dfsSerialize(root, res);
        return String.join(",", res);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] vals = data.split(",");
        int[] i = {0};
        return dfsDeserizalize(vals, i);
        
    }
    public TreeNode dfsDeserizalize(String[] vals, int[] i){
        if(vals[i[0]].equals("N")){
            i[0]++;
            return null;
        }
        TreeNode node = new TreeNode(Integer.parseInt(vals[i[0]]));
        i[0]++;
        node.left = dfsDeserizalize(vals, i);
        node.right = dfsDeserizalize(vals, i);
        return node;
    }
}
