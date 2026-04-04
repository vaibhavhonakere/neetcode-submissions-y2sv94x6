class Solution {
    /**
     * @param {character[][]} board
     * @param {string} word
     * @return {boolean}
     */
    exist(board, word) {
        const ROWS = board.length
        const COLS = board[0].length
        const path = new Set();
        const dfs = (r,c,i) => {
            if(i === word.length){
                return true;
            }
            if(r >= ROWS || c >= COLS || 0 > r || 0 > c 
                || path.has(`${r},${c}`) || board[r][c] !== word[i]){
                    return false
                }
            path.add(`${r},${c}`)
            const ret = dfs(r + 1, c, i + 1) || 
                        dfs(r, c + 1, i + 1) ||
                        dfs(r - 1, c, i + 1) ||
                        dfs(r, c - 1, i + 1)
            path.delete(`${r},${c}`)
            return ret
        }
        for(let i = 0; i < ROWS; i++){
            for(let j = 0; j < COLS; j++){
                if(board[i][j] == word[0] && dfs(i,j,0)){
                    return true
                }
            }
        }
        return false
    }
}
