class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    maxAreaOfIsland(grid) {
        let ROWS = grid.length
        let COLS = grid[0].length
        let seen = new Set();
        let ret = 0;
        const dfs = ((r,c,size) =>{
            if(r < 0 || c < 0 || r >= ROWS || c >= COLS
             || grid[r][c] !== 1 || seen.has(`${r},${c}`)){
                return 0
            }
            seen.add(`${r},${c}`)
            return 1 + dfs(r + 1, c, size + 1) + dfs(r, c + 1,size + 1) + dfs(r - 1, c, size + 1) + dfs(r, c - 1,size + 1)
        })
        for(let i = 0; i < grid.length; i++){
            for(let j = 0; j < grid[0].length; j++){
                if(!seen.has(`${i},${j}`) && grid[i][j] === 1){
                    let check = dfs(i,j,1)
                    console.log(check, i, j)
                    ret = Math.max(ret, check)
                }
            }
        }
        return ret
    }
}
