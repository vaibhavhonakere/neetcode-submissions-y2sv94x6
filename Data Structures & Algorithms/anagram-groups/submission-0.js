class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const cache = new Map();
        for(let i=0; i < strs.length; i++){
            let key = strs[i].split("").sort().join()
            if(cache.has(key)){
                let val = cache.get(key)
                val.push(strs[i])
                cache.set(key, val)
            }else{
                let first = [strs[i]]
                cache.set(key, first)
            }
        }
        let ret = []
        for(const [_, value] of cache){
            ret.push(value);
        }
        return ret;
    }
}
