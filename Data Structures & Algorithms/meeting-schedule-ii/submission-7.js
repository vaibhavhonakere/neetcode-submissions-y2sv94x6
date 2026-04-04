/**
 * Definition of Interval:
 * class Interval {
 *   constructor(start, end) {
 *     this.start = start;
 *     this.end = end;
 *   }
 * }
 */

class Solution {
    /**
     * @param {Interval[]} intervals
     * @returns {number}
     */
    minMeetingRooms(intervals) {
        let start = [], end = []
        for(let int of intervals){
            start.push(int.start)
            end.push(int.end)
        }
        start.sort((a,b) => a - b)
        end.sort((a,b) => a - b)
        let left = 0, right = 0;
        let maxRooms = 0;
        let curRooms = 0;
        while(left < start.length && right < end.length){
            if(start[left] < end[right]){
                curRooms += 1
                left += 1
            }else{
                curRooms -= 1
                right += 1
            }
            maxRooms = Math.max(maxRooms, curRooms)
        }
        return maxRooms
    }
}
