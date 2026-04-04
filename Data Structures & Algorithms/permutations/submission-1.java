class Solution {
    public List<List<Integer>> permute(int[] nums) {
        Integer[] integerArray = Arrays.stream(nums).boxed().toArray(Integer[]::new);
        return dfs(Arrays.asList(integerArray));
    }
    private List<List<Integer>> dfs(List<Integer> n){
        if(n.size() == 0){
            List<List<Integer>> listOfLists = new ArrayList<>();
            // Add an empty ArrayList to it
            listOfLists.add(new ArrayList<>());
            return listOfLists;
        }
        List<Integer> sliced = new ArrayList<>(n.subList(1, n.size()));
        System.out.println(sliced);
        List<List<Integer>> perms = dfs(sliced);
        System.out.println("first " + perms);
        List<List<Integer>> ret = new ArrayList<>();
        for(List<Integer> p: perms){
            System.out.println("second " + p);
            for(int i=0; i < p.size() + 1; i++){
                List<Integer> p_copy = new ArrayList<>(p);
                p_copy.add(i, n.get(0));
                ret.add(p_copy);
            }
        }
        return ret;

    }
}
