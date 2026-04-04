class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0){
            return 0;
        }
        Integer[] numsWrapper = Arrays.stream(nums).boxed().toArray(Integer[]::new);
        HashSet<Integer> sequence = new HashSet<>(Arrays.asList(numsWrapper));
        int longest_sequence = 1;
        for(int n: nums){
            if(sequence.contains(n - 1)){
                int num = n - 1;
                int count = 1;
                while(sequence.contains(num)){
                    count++;
                    longest_sequence = Math.max(count, longest_sequence);
                    num--;
                }
            }
        }
        return longest_sequence;
    }
}
