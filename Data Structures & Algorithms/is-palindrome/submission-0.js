class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    
    isPalindrome(s) {
        let i = 0;
        let j = s.length - 1;
        while(i < j){
            while(i < j && !this.alphaNum(s[i])){
                i++;
            }
            while(i < j && !this.alphaNum(s[j])){
                j--;
            }
            if(s[i].toLowerCase() !== s[j].toLowerCase()){
                return false;
            }
            i++;
            j--;
        }
        return true;

    }
    alphaNum(c) {
        return (c >= 'A' && c <= 'Z' || 
                c >= 'a' && c <= 'z' || 
                c >= '0' && c <= '9');
    }
}
