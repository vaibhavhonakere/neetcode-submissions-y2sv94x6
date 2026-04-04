class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
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
        for(int i=0; i < numCourses; i++){
            if(!dfs(i,map, visited)){
                return false;
            }
        }
        return true;
    }
    public boolean dfs(int i, HashMap<Integer, List<Integer>> map,HashSet<Integer> visited){
        if(map.get(i).isEmpty()){
            return true;
        }
        if(visited.contains(i)){
            return false;
        }

        visited.add(i);
        for(int p: map.get(i)){
            if(!dfs(p, map, visited)){
                return false;
            }
        }

        visited.remove(i);
        map.put(i, new ArrayList<>());
        return true;
    }
}
