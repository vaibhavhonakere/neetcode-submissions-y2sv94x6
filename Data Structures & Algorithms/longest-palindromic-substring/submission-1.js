class Solution {
    /**
     * @param {string} s
     * @return {string}
     */
    isPalindrome(left, right, s){
        let ret = [0,0]
        while(left >= 0 && right < s.length){
            console.log(s[left], s[right], left, right)
            if(s[left] === s[right]){
                ret = [left, right]
                left--;
                right++;
            }else{
                break;
            }
        }
        return ret
    }
    longestPalindrome(s) {
        let start = 0
        let end = 0
        let maxVal = -1
        for(let i = 0; i < s.length; i++){
            let l = i
            let r = i
            let [left, right] = this.isPalindrome(l,r,s)
            if(right - left + 1 > maxVal){
                start = left
                end = right
                maxVal = right - left + 1
            }
            l = i;
            r = i + 1;
            [left, right] = this.isPalindrome(l,r,s)
            if(right - left + 1 > maxVal){
                start = left
                end = right
                maxVal = right - left + 1
            }
        }
        return s.substring(start, end + 1)
    }
}
