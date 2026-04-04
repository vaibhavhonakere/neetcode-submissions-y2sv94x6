class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number[][]}
     */
    merge(intervals) {
        intervals.sort((a,b) => a[0] - b[0])
        let ret = [intervals[0]]
        for(let [x,y] of intervals){
            if(x <= ret[ret.length - 1][1]){
                let minVal = Math.min(x, ret[ret.length - 1][0])
                let maxVal = Math.max(y, ret[ret.length - 1][1])
                ret[ret.length - 1][0] = minVal
                ret[ret.length - 1][1] = maxVal
            }else{
                ret.push([x,y])
            }
        }
        return ret
    }
}
