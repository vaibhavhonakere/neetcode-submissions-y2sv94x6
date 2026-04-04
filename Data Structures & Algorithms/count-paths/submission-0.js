class Solution {
    /**
     * @param {number} m
     * @param {number} n
     * @return {number}
     */
    uniquePaths(m, n) {
        let cache = new Map();
        const dfs = ((r,c) => {
            if(r == m - 1 && c == n - 1){
                return 1
            }else if(r > m || c > n || r < 0 || c < 0){
                return 0
            }else if(cache.has(`${r},${c}`)){
                return cache.get(`${r},${c}`)
            }
            cache.set(`${r},${c}`, dfs(r + 1, c) + dfs(r, c + 1))
            console.log(cache.get(`${r},${c}`), r, c)
            return cache.get(`${r},${c}`)
        })
        return dfs(0,0)
    }
}
