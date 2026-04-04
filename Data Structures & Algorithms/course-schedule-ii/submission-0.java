class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        HashMap<Integer, List<Integer>> map = new HashMap<>();

        for (int i = 0; i < numCourses; i++) {
            map.put(i, new ArrayList<>());
        }

        for(int[] point: prerequisites){
            if(map.containsKey(point[0])){
                List<Integer> temp_2 = map.get(point[0]);
                temp_2.add(point[1]);
                map.put(point[0], temp_2);
            }else{
                List<Integer> temp = new ArrayList<>();
                temp.add(point[1]);
                map.put(point[0], temp);
            }
        }
        HashSet<Integer> visited = new HashSet<>();
        HashSet<Integer> seen = new HashSet<>();
        List<Integer> ret = new ArrayList<>();
        for(int i=0; i < numCourses; i++){
            if(!dfs(i,map, visited, seen, ret)){
                return new int[0];
            }
        }
        int[] intArray = new int[ret.size()];
        for (int i = 0; i < ret.size(); i++) {
            intArray[i] = ret.get(i);
        }
        return intArray;
    }
    public boolean dfs(int i, HashMap<Integer, List<Integer>> map,HashSet<Integer> visited, HashSet<Integer> seen, List<Integer> list){
        if(visited.contains(i)){
            return false;
        }
        if(seen.contains(i)){
            return true;
        }
        seen.add(i);
        visited.add(i);
        for(int p: map.get(i)){
            if(!dfs(p, map, visited, seen, list)){
                return false;
            }
        }
        visited.remove(i);
        list.add(i);
        return true;
    }
}
