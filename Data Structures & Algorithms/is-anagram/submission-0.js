class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length !== t.length){
            return false;
        }
        let left = s.split("").sort().join();
        let right = t.split("").sort().join();
        return left == right;
    }
}
