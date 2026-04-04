class Solution {
    /**
     * @param {number[]} stones
     * @return {number}
     */
    lastStoneWeight(stones) {
        let maxHeap = new MaxPriorityQueue();
        for(let s of stones){
            maxHeap.enqueue(s)
        }
        maxHeap.enqueue(0)
        while(maxHeap.size() > 1){
            let first = maxHeap.dequeue()
            let second = maxHeap.dequeue()
            let diff = Math.abs(first - second)
            if(diff !== 0){
                maxHeap.enqueue(diff)
            }
        }
        return maxHeap.dequeue()

    }
}
