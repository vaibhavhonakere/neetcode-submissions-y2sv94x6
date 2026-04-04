class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        const mySet = new Set();
        let l = 0;
        let ret = 0;
        for(let r=0; r < s.length; r++){
            while(mySet.has(s[r])){
                let char = s[l]
                mySet.delete(char)
                l++;
            }
            mySet.add(s[r])
            ret = Math.max(ret, r - l + 1)
        }
        return ret;
    }
}
