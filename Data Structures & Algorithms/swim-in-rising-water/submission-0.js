class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    swimInWater(grid) {
        const N = grid.length;
        const minHeap = new MinPriorityQueue((points)=>points[0])
        let visted = new Set();
        const dirs = [
            [0,1],
            [1,0],
            [-1,0],
            [0,-1]
        ]
        minHeap.push([grid[0][0], 0,0])
        visted.add("0,0");
        while(minHeap.size() > 0){
            const [t,r,c] = minHeap.dequeue();
            if(r == N - 1 && c == N - 1){
                return t;
            }
            for(let [dr, dc] of dirs){
                let newX = dr + r
                let newY = dc + c
                if(newX < 0 || newY < 0 ||
                   newX >= N || newY >= N || visted.has(`${newX},${newY}`)){
                    continue
                   }
                visted.add(`${newX},${newY}`)
                minHeap.enqueue([Math.max(t, grid[newX][newY]), newX, newY])
            }
        }
        return -1
    }
}
