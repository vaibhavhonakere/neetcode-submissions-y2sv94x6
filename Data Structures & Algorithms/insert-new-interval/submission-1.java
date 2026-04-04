class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> ret = new ArrayList<>();
        // ret.add(new int[]{Integer.MAX_VALUE, Integer.MIN_VALUE});
        // res = []
        // for s, e in intervals:
        //     if(s <= newInterval[0] and newInterval[0] <= e) or (newInterval[0] <= s and s <= newInterval[1]):
        //         newInterval[0], newInterval[1] = min(s, newInterval[0]), max(e, newInterval[1])
        //     elif(s <= newInterval[0] and e <= newInterval[0]):
        //         res.append([s,e])
        //     else:
        //         res.append([newInterval[0], newInterval[1]])
        //         newInterval[0], newInterval[1] = s,e
        // res.append(newInterval)
        // return res


        
        for(int i = 0; i < intervals.length; i++){
            if((intervals[i][0] <= newInterval[0] && newInterval[0] <= intervals[i][1])
             ||(intervals[i][0] >= newInterval[0] && intervals[i][0] <= newInterval[1])){
                newInterval[0] = Math.min(intervals[i][0], newInterval[0]);
                newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
                // System.out.println("here");
            }else if(intervals[i][0] <= newInterval[0] && intervals[i][1] <= newInterval[0]){
                ret.add(new int[]{intervals[i][0], intervals[i][1]});
            }else{
                ret.add(new int[]{newInterval[0], newInterval[1]});
                newInterval[0] = intervals[i][0];
                newInterval[1] = intervals[i][1];
            }
        }
        ret.add(new int[]{newInterval[0], newInterval[1]});
        int[][] new_ret = new int[ret.size()][2];
        int i = 0;
        for(int[] p: ret){
            new_ret[i] = p;
            i += 1;
        }
        return new_ret;
    }
}
