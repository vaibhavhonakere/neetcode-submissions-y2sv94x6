class Solution {
    /**
     * @param {number[][]} grid
     */
    islandsAndTreasure(grid) {
        let ROWS = grid.length;
        let COLS = grid[0].length;
        let visit = new Set()
        const directions = [[1, 0], [-1, 0], [0, 1], [0, -1]];
        let queue = new Queue();
        
        for(let i = 0; i < ROWS; i++){
            for(let j = 0; j < COLS; j++){
                if(grid[i][j] == 0){
                    queue.push([i,j])
                    visit.add(i + " " +j)
                }
            }
        }
        let dist = 0;
        console.log(queue, visit)
        while(!queue.isEmpty()){
            let length = queue.size()
            for(let i = 0; i < length; i++){
                let [r,c] = queue.pop()
                grid[r][c] = dist;
                for(let [x,y] of directions){
                    let newX = r + x
                    let newY = y + c
                    if(newX >= ROWS || newY >= COLS || newX < 0 || newY < 0 ||
                        visit.has(newX + " " + newY) || grid[newX][newY] === -1){
                            continue
                    }
                    visit.add(newX + " " + newY)
                    queue.push([newX, newY])
                }
            }
            dist += 1
        }
    }
}
