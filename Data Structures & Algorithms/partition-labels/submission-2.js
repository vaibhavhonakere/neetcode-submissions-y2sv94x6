class Solution {
    /**
     * @param {string} S
     * @return {number[]}
     */
    partitionLabels(S) {
        let cache = new Map()
        for(let i = 0; i < S.length; i++){
            cache.set(S[i], i)
        }
        let ret = []
        let maxInd = 0
        let dist = 0
        for(let i = 0; i < S.length; i++){
            dist += 1
            maxInd = Math.max(maxInd, cache.get(S[i]))
            if(i === maxInd){
                ret.push(dist)
                dist = 0
            }
        }
        return ret
    }
}
