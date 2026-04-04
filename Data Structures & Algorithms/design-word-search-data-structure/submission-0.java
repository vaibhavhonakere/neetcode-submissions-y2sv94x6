class WordDictionary {
    PrefixTreeNode root;

    class PrefixTreeNode{
        public int value;
        public boolean isEnd;
        public PrefixTreeNode[] children;
        public PrefixTreeNode(int val){
            this.value = val;
            this.isEnd = false;
            this.children = new PrefixTreeNode[26];
        }
    }

    public WordDictionary() {
        this.root = new PrefixTreeNode(' ');
    }

    public void addWord(String word) {
        PrefixTreeNode curr = this.root;
        for(char c: word.toCharArray()){
            if(curr.children[c - 'a'] == null){
                curr.children[c - 'a'] = new PrefixTreeNode(c);
            }
            curr = curr.children[c - 'a'];
        }
        curr.isEnd = true;
    }

    public boolean search(String word) {
        return dfs(word, 0, root);
    }
    private boolean dfs(String word, int j, PrefixTreeNode root){
        PrefixTreeNode curr = root;
        for(int i = j; i < word.length(); i++){
            char c = word.charAt(i);
            if(c == '.'){
                for(PrefixTreeNode child: curr.children){
                    if(child != null && dfs(word, i + 1, child)){
                        return true;
                    }
                }
                return false;
            }else{
                if(curr.children[c - 'a'] == null){
                    return false;
                }
                curr = curr.children[c - 'a'];
            }
        }
        return curr.isEnd;
    }
}
