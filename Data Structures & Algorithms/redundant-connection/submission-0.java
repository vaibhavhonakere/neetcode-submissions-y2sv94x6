class Solution {
    private int[] par;
    private int[] rank;

    public int[] findRedundantConnection(int[][] edges) {
        this.par = new int[edges.length + 1];
        this.rank = new int[edges.length + 1];
        for(int i = 1; i < edges.length + 1; i++){
            this.par[i] = i;
            this.rank[i] = 1;
        }

        for(int[]p : edges){
            if(union(p[0], p[1]) == 0){
                return p;
            }
        }
        return new int[0];
    }
    private int find(int node){
        int result = node;
        while(par[result] != result){
            result = par[result];
        }
        return result;
    }
    private int union(int n1, int n2){
        int first = find(n1);
        int second = find(n2);

        if(par[first] == par[second]){
            return 0;
        }
        if(rank[first] > rank[second]){
            par[second] = first;
            rank[first] += rank[second];
        }else{
            par[first] = second;
            rank[second] += rank[first];
        }
        return 1;
    }
}
