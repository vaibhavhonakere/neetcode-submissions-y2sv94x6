class Solution {
    private List<int[]> pacific;
    private List<int[]> atlantic;
    private int ROWS;
    private int COLS;

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> ret = new ArrayList<>();
        this.ROWS = heights.length;
        this.COLS = heights[0].length;
        // Find the visited nodes from the pacific 
        // top left to top right
        // top left to bottom left
        this.pacific = new ArrayList<>();
        for(int i=0;i<heights.length;i++){
            for(int j=0;j<heights[0].length;j++){
                if(i == 0 || (i != 0 && j == 0)){
                    this.pacific.add(new int[]{i,j});
                }
            }
        }
        HashSet<List<Integer>> pacific_Set = new HashSet<>();
        for(int[] point: this.pacific){
            dfsAtlantic(point[0], point[1], heights[point[0]][point[1]], heights, pacific_Set);
        }


        // Find the visited nodes from the atlantic 
        // top right to bottom right
        // bottom left to bottom right
        this.atlantic = new ArrayList<>();
        for(int i=0;i<heights.length;i++){
            for(int j=0;j<heights[0].length;j++){
                if(i == (heights.length - 1) || (i != heights.length - 1 && j == (heights[0].length - 1))){
                    this.atlantic.add(new int[]{i,j});
                }
            }
        }
        HashSet<List<Integer>> atlantic_Set = new HashSet<>();
        for(int[] point: this.atlantic){
            dfsAtlantic(point[0], point[1], heights[point[0]][point[1]], heights, atlantic_Set);
        }
        for(List<Integer> p_1 : atlantic_Set){
            for(List<Integer> p_2 : pacific_Set){
                if(p_1.equals(p_2)){
                    // List<Integer> temp = new ArrayList<>();
                    // temp.add(p_1[0]);
                    // temp.add(p_2[0]);
                    ret.add(p_1);
                }
            }
        }
        return ret;


    }
    private void dfsAtlantic(int i, int j, int prevVal, int[][] heights, HashSet<List<Integer>> seen){
        if(i == ROWS || i < 0 || j < 0 || j == COLS || seen.contains(Arrays.asList(i, j)) || prevVal > heights[i][j]){
            return;
        }
        seen.add(Arrays.asList(i, j));
        dfsAtlantic(i + 1, j, heights[i][j], heights, seen);
        dfsAtlantic(i - 1, j, heights[i][j], heights, seen);
        dfsAtlantic(i, j + 1, heights[i][j], heights, seen);
        dfsAtlantic(i, j - 1, heights[i][j], heights, seen);
        return;
    }

}
