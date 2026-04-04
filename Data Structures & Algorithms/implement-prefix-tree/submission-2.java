class PrefixTree {
    // PrefixTreeNode root;

    // public PrefixTree(){
    //     root = new PrefixTreeNode(' ');
    // }
    class PrefixTreeNode{
        private char value;
        private boolean isWord;
        private PrefixTreeNode[] children;
        public PrefixTreeNode(char val){
            this.value = val;
            this.isWord = false;
            this.children = new PrefixTreeNode[26];
        }
    }
    PrefixTreeNode root;

    public PrefixTree(){
        this.root = new PrefixTreeNode(' ');
    }

    public void insert(String word) {
        PrefixTreeNode curr = root;
        for(char x: word.toCharArray()){
            if(curr.children[x - 'a'] == null){
                curr.children[x - 'a'] = new PrefixTreeNode(x);
            }
            curr = curr.children[x - 'a'];
        }
        curr.isWord = true;
    }

    public boolean search(String word) {
        PrefixTreeNode curr = root;
        for(char x: word.toCharArray()){
            if(curr.children[x - 'a'] == null){
                return false;
            }
            curr = curr.children[x - 'a'];
        }
        return curr.isWord;
    }

    public boolean startsWith(String prefix) {
        PrefixTreeNode curr = root;
        for(char x: prefix.toCharArray()){
            if(curr.children[x - 'a'] == null){
                return false;
            }
            curr = curr.children[x - 'a'];
        }
        return true;
    }
}
