class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparing(a -> a[0]));
        for(int[] p: points){
            int dist = p[0] * p[0] + p[1] * p[1];
            minHeap.offer(new int[]{dist, p[0], p[1]});
        }
        
        int [][] ret = new int[k][2];
        for(int i = 0; i < k; i++){
            int[] point = minHeap.poll();
            ret[i] = new int[]{point[1], point[2]};
        }
        return ret;

    }
}
