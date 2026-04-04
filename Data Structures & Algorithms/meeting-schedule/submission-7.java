/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

class Solution {
    public boolean canAttendMeetings(List<Interval> intervals) {
        boolean ret = true;
        if(intervals.size() <= 1){
            return true;
        }
        intervals.sort(Comparator.comparingInt(interval -> interval.start));
        Interval first = intervals.get(0);
        for(int i = 1; i < intervals.size(); i++){
            if(intervals.get(i).start < first.end){
                return false;
            }else{
                first.start = intervals.get(i).start;
                first.end = intervals.get(i).end;
            }   
        }

        return ret;
    }
}
