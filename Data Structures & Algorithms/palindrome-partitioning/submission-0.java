class Solution {
    private int lengthOfStr;
    private List<List<String>> ret;

    public List<List<String>> partition(String s) {
        this.lengthOfStr = s.length();
        this.ret = new ArrayList<>();
        dfs(0, new ArrayList<>(), s);
        return this.ret;
    }
    private boolean checkPalindrome(String s){
        int left = 0;
        int right = s.length() - 1;
        while(left < right){
            if(s.charAt(left) != s.charAt(right)){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
    private void dfs(int index, List<String> subset, String s){
        if(index == lengthOfStr){
            ret.add(new ArrayList<>(subset));
            return;
        }
        for(int i = index; i < lengthOfStr; i++){
            if(checkPalindrome(s.substring(index, i + 1))){
                subset.add(s.substring(index, i+1));
                dfs(i + 1, subset, s);
                subset.remove(s.substring(index, i+1));
            }
        }
    }
}
