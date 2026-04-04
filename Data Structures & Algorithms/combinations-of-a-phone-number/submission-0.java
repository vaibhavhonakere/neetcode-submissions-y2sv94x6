class Solution {
    private List<String> ret;
    private int length;
    private String digits;
    public List<String> letterCombinations(String digits) {
        if(digits.length() == 0){
            return new ArrayList<>();
        }
        HashMap<String, String> map = new HashMap<>();
        this.length = digits.length();
        this.digits = digits;
        this.ret = new ArrayList<>();
        map.put("2", "abc");
        map.put("3", "def");
        map.put("4", "ghi");
        map.put("5", "jkl");
        map.put("6", "mno");
        map.put("7", "pqrs");
        map.put("8", "tuv");
        map.put("9", "wxyz");
        dfs(0, new StringBuilder(), map);
        return this.ret;

    }
    public void dfs(int index, StringBuilder subset, HashMap<String, String> map){
        if(index == length){
            ret.add(subset.toString());
            return;
        }
        // System.out.println("The character " + this.digits.charAt(index));
        // System.out.println("The map value " + map.get(Character.toString(this.digits.charAt(index))));
        //System.out.println("The character length " + this.digits.charAt(index).length());

        String value = map.get(Character.toString(this.digits.charAt(index)));
        int l = value.length();
        for(int i=0; i < l; i++){
            subset.append(value.charAt(i));
            dfs(index + 1, subset, map);
            subset.deleteCharAt(subset.length() - 1);
        }
    }
}
