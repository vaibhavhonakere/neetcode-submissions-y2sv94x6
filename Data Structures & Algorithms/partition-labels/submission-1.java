class Solution {
    public List<Integer> partitionLabels(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            map.put(s.charAt(i), i);
        }
        List<Integer> ret = new ArrayList<>();
        int count = 0;
        int target = 0;
        for(int i = 0; i < s.length(); i++){
            target = Math.max(target, map.get(s.charAt(i)));
            count += 1;
            if(i == target){
                ret.add(count);
                count = 0;
            }
        }
        return ret;
        
    }
}
