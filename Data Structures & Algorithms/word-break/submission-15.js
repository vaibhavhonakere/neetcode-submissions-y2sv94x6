class Solution {
    /**
     * @param {string} s
     * @param {string[]} wordDict
     * @return {boolean}
     */
    wordBreak(s, wordDict) {
        const cache = new Map();
        cache.set(s.length, true)
        const dfs = ((i)=>{
            if(i >= s.length){
                return true
            }
            if(cache.has(i)){
                return cache.get(i)
            }
            let ret = false
            for(let j = 0; j < wordDict.length; j++){
               let checkWord = wordDict[j] 
               let length = checkWord.length
               if(s.substring(i, i + length) === checkWord && dfs(i + length)){
                    ret = true
               }
            }
            cache.set(i,ret)
            return cache.get(i)
        })
        return dfs(0)
    }
}
