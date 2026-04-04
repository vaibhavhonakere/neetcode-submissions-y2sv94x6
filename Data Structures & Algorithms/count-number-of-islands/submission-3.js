class Solution {
    /**
     * @param {character[][]} grid
     * @return {number}
     */
    numIslands(grid) {
        let ROWS = grid.length
        let COLS = grid[0].length
        let seen = new Set();
        let count = 0;

        const dfs = ((r,c) =>{
            if(r < 0 || c < 0 || r >= ROWS || c >= COLS
             || grid[r][c] !== "1" || seen.has(`${r},${c}`)){
                return
            }
            seen.add(`${r},${c}`)
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
            return
        })
        for(let i = 0; i < grid.length; i++){
            for(let j = 0; j < grid[0].length; j++){
                if(!seen.has(`${i},${j}`) && grid[i][j] === "1"){
                    dfs(i,j)
                    count += 1
                }
            }
        }
        return count
    }
}
