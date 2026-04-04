class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        // monotonic increasing stack
        // [(40,5), (28, 2)]
        // [1,4, 1, 2, 1, 0, 0]
        let stack = []
        const arr = new Array(temperatures.length).fill(0)
        for(let i = 0; i < temperatures.length; i++){
            while(stack.length > 0 && stack[stack.length - 1][0] < temperatures[i]){
                let lastElement = stack.pop();
                arr[lastElement[1]] = i - lastElement[1]
            }
            stack.push([temperatures[i], i])
        }
        return arr;
    }
}
