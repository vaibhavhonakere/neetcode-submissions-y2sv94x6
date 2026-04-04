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
    public int minMeetingRooms(List<Interval> intervals) {
        List<Integer> start_times = new ArrayList<>();
        List<Integer> end_times = new ArrayList<>();

        for(Interval p: intervals){
            start_times.add(p.start);
            end_times.add(p.end);
        }

        Collections.sort(start_times);
        Collections.sort(end_times);
        int start = 0;
        int end = 0;
        int curr = 0;
        int maxMeetingRooms = 0;
        while(start < start_times.size()){
            if(start_times.get(start) < end_times.get(end)){
                curr += 1;
                start += 1;
            }else{
                end += 1;
                curr -= 1;
            }
            maxMeetingRooms = Math.max(maxMeetingRooms, curr);
        }
        return maxMeetingRooms;
    }
}
