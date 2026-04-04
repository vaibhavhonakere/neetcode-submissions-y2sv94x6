class Solution {
    /**
     * @param {number[][]} intervals
     * @param {number[]} newInterval
     * @return {number[][]}
     */
    insert(intervals, newInterval) {
        let ret = []
        // intervals.sort((a, b) => a - b)
        for(let [x,y] of intervals){
            if(x <= newInterval[0] && newInterval[0] <= y || newInterval[0] <= x && x <= newInterval[1]){
                newInterval[0] = Math.min(newInterval[0], x)
                newInterval[1] = Math.max(newInterval[1], y)
            }else if(y < newInterval[0]){
                ret.push([x,y])
            }
            else{
                ret.push([newInterval[0], newInterval[1]])
                newInterval[0] = x
                newInterval[1] = y
            }
        }
        ret.push(newInterval)
        return ret
    }
}
