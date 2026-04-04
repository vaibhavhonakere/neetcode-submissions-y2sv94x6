class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        // Length - maxFreq > k
        let cache = new Map();
        let maxFreq = -1;
        let ret = 0;
        let l = 0;
        for(let r = 0; r < s.length; r++){
            cache.set(s[r], (cache.get(s[r]) || 0) + 1);
            maxFreq = Math.max(cache.get(s[r]), maxFreq);
            if((r - l + 1) - maxFreq > k){
                cache.set(s[l], cache.get(s[l]) - 1)
                // if(cache.get(char) == 0){
                //     cache.delete(char)
                // }
                l++;
            }
            console.log("here 2")
            ret = Math.max(ret, r - l + 1)
        }
        return ret;
    }
}
