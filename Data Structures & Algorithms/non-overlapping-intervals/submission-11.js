class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number}
     */
    eraseOverlapIntervals(intervals) {
        intervals.sort((a,b) => a[1] - b[1]);
        let inital = intervals[0]
        let res = 0
        for(let i = 1; i < intervals.length; i++){
            if(intervals[i][0] < inital[1]){
                res++
            }else{
                inital[1] = intervals[i][1]
            }
        }
        return res
    }
}
