class Solution {
    public boolean validTree(int n, int[][] edges) {
        HashMap<Integer, List<Integer>> map = new HashMap<>();

        if (n == 1) return edges.length == 0;
    
        if (edges.length == 0) return false;

        for (int i = 0; i < n; i++) {
            map.put(i, new ArrayList<>());
        }

        for(int[] point: edges){
            List<Integer> temp_1 = map.get(point[0]);
            temp_1.add(point[1]);
            map.put(point[0], temp_1);
            List<Integer> temp_2 = map.get(point[1]);
            temp_2.add(point[0]);
            map.put(point[1], temp_2);
        }
        boolean flag = false;
        HashSet<Integer> visited = new HashSet<>();
        if(!dfs(edges[0][0], -1, map, visited)){
            return false;
        }
        return visited.size() == n;
    }
    public boolean dfs(int i, int prev, HashMap<Integer, List<Integer>> map,HashSet<Integer> visited){
        if(visited.contains(i)){
            return false;
        }

        visited.add(i);
        for(int p: map.get(i)){
            if(p == prev){
                continue;
            }
            if(!dfs(p, i, map, visited)){
                return false;
            }
        }
        return true;
    }
}
