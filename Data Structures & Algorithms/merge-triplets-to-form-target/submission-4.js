class Solution {
    /**
     * @param {number[][]} triplets
     * @param {number[]} target
     * @return {boolean}
     */
    mergeTriplets(triplets, target) {
        let first = false
        let second = false
        let third = false
        let entry = triplets[0]
        for(let [x,y,z] of triplets){
            if(x > target[0] || y > target[1] || z > target[2]){
                continue
            }
            if(x === target[0]){
                first = true
            }
            if(y === target[1]){
                second = true
            }
            if(z === target[2]){
                third = true
            }

        }
        return (first && second && third)
    }
}
