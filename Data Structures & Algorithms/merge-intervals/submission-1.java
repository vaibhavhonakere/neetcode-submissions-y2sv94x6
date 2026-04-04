class Solution {
    public int[][] merge(int[][] intervals) {
        List<int[]> ret = new ArrayList<>();
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        ret.add(new int[]{intervals[0][0], intervals[0][1]});
        // intervals.sort(Comparator.comparingInt(a -> a[0]));

        for(int i = 1; i < intervals.length; i++){
            if(ret.get(ret.size() - 1)[0] <= intervals[i][0] && intervals[i][0] <= ret.get(ret.size() - 1)[1]){
                ret.get(ret.size() - 1)[0] = Math.min(ret.get(ret.size() - 1)[0], intervals[i][0]);
                ret.get(ret.size() - 1)[1] = Math.max(ret.get(ret.size() - 1)[1], intervals[i][1]);
            }else{
                ret.add(new int[]{intervals[i][0], intervals[i][1]});
            }
        }

        int[][] new_ret = new int[ret.size()][2];
        int i = 0;
        for(int[] p: ret){
            new_ret[i] = p;
            i += 1;
        }
        return new_ret;
    }
}
