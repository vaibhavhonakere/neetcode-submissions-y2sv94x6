class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        const cache = new Map();
        for(let i=0; i < numbers.length; i++){
            let diff = target - numbers[i]
            if(cache.has(diff)){
                return [cache.get(diff)+1, i+1,]
            }
            cache.set(numbers[i], i);
        }
    }
}
