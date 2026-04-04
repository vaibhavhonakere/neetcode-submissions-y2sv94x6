class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    findKthLargest(nums, k) {
        const maxHeap = new MinPriorityQueue()
        for(let n of nums){
            maxHeap.enqueue(n)
        }
        while(maxHeap.size() > k){
            maxHeap.dequeue()
        }
        return maxHeap.front()
    }
}
