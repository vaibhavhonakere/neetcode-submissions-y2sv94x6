class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        HashMap<Integer, List<int[]>> map = new HashMap<>();
        for(int[] t: times){
            int s = t[0], e = t[1], dist = t[2];
            if(!map.containsKey(s)){
                map.put(s, new ArrayList<>());
            }
            map.get(s).add(new int[]{dist, e});
        }
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        HashSet<Integer> visited = new HashSet<>();
        minHeap.offer(new int[]{0,k});
        int res = 0;

        while(!minHeap.isEmpty()){
            int[] val = minHeap.poll();
            int dist = val[0];
            int node = val[1];
            if(visited.contains(node)){
                continue;
            }
            res = dist;
            visited.add(node);
            if(map.get(node) == null){
                continue;
            }
            for(int[] p: map.get(node)){
                if(visited.contains(p[1])){
                    continue;
                }
                minHeap.offer(new int[]{dist + p[0], p[1]});
            }
        }
        return (visited.size() == n) ? res : -1;
    }
}
