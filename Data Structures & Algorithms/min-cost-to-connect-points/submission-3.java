class Solution {
    public int minCostConnectPoints(int[][] points) {
        HashMap<Integer, List<int[]>> map = new HashMap<>();
        for(int i = 0; i < points.length; i++){
            int x1 = points[i][0];
            int y1 = points[i][1];
            for(int j = i + 1; j < points.length; j++){
                int x2 = points[j][0];
                int y2 = points[j][1];
                int manhattan_Distance = Math.abs(x1 - x2) + Math.abs(y1 - y2); 
                //map.computeIfAbsent(i, k -> new ArrayList<>()).add(new int[]{manhattan_Distance, j});
                //map.computeIfAbsent(j, k -> new ArrayList<>()).add(new int[]{manhattan_Distance, i});
                if(!map.containsKey(i)){
                    map.put(i, new ArrayList<>());
                }
                map.get(i).add(new int[]{manhattan_Distance, j});
                if(!map.containsKey(j)){
                    map.put(j, new ArrayList<>());
                }
                map.get(j).add(new int[]{manhattan_Distance, i});
            }
        }
        int ret = 0;
        HashSet<Integer> visit = new HashSet<>();
        PriorityQueue<int[]> queue = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        queue.offer(new int[]{0,0});
        while(visit.size() < points.length){
            int[] val = queue.poll();
            int dist = val[0];
            int node = val[1];
            if(visit.contains(node)){
                continue;
            }
            ret += dist;
            visit.add(node);
            if(map.get(node) == null){
                continue;
            }
            for(int[] p: map.get(node)){
                if(visit.contains(p[1])){
                    continue;
                }
                queue.add(new int[]{p[0], p[1]});
            }
        }
        return ret;
    }
}
