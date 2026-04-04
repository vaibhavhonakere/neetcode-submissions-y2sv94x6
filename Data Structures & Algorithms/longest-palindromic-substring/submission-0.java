class Solution {
    public String longestPalindrome(String s) {
        int longest = -1;
        String ret = "";
        for(int i = 0; i < s.length(); i++){
            int left_1 = i;
            int right_1 = i;
            while(left_1 >= 0 && right_1 < s.length()){
                if(s.charAt(left_1) == s.charAt(right_1)){
                    if(right_1 - left_1 + 1 >= longest){
                        longest = Math.max(longest,right_1 - left_1 + 1);
                        ret = s.substring(left_1, right_1 + 1);
                    }
                    left_1 -= 1;
                    right_1 += 1;
                }else{
                    break;
                }
            }
            int left_2 = i;
            int right_2 = i + 1;
            while(left_2 >= 0 && right_2 < s.length()){
                if(s.charAt(left_2) == s.charAt(right_2)){
                    if(right_2 - left_2 + 1 >= longest){
                        longest = Math.max(longest,right_2 - left_2 + 1);
                        ret = s.substring(left_2, right_2 + 1);
                    }
                    left_2 -= 1;
                    right_2 += 1;
                }else{
                    break;
                }
            }
        }
        return ret;
    }
}
