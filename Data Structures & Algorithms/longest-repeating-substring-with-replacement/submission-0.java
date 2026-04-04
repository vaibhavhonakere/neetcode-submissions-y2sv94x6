class Solution {
    public int characterReplacement(String s, int k) {
        // the key thing is length - maxFreq - k
        HashMap<Character, Integer> freq_to_Num = new HashMap<>();
        int left = 0;
        int maxFreq = -1;
        int maxLength = -1;
        for(int right = 0; right < s.length(); right++){
            if(!freq_to_Num.containsKey(s.charAt(right))){
                freq_to_Num.put(s.charAt(right), 1);
            }else{
                freq_to_Num.put(s.charAt(right), 1 + freq_to_Num.get(s.charAt(right)));
            }
            maxFreq = Math.max(maxFreq, freq_to_Num.values().stream().max(Integer::compare).orElse(Integer.MIN_VALUE));
            //maxFreq = math.max(maxFreq, freq_to_Num.values().stream().max(Integer::compare).orElse(Integer.MIN_VALUE));
            if((right - left + 1) - maxFreq > k){
                if(freq_to_Num.get(s.charAt(left)) == 1){
                    freq_to_Num.remove(s.charAt(left));
                }else{
                    freq_to_Num.put(s.charAt(left), freq_to_Num.get(s.charAt(left)) - 1);
                }
                left += 1;
            }
            maxLength = Math.max(maxLength, (right - left + 1));
        }
        return maxLength;
    }
}
