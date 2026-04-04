class MedianFinder {
    constructor() {
        this.minHeap = new MinPriorityQueue();
        this.maxHeap = new MaxPriorityQueue();
    }
    /**
     *
     * @param {number} num
     * @return {void}
     */
    addNum(num) {
        if(this.minHeap.size() > 0 && num > this.minHeap.front()){
            let node = this.minHeap.dequeue()
            this.maxHeap.enqueue(node)
            this.minHeap.enqueue(num)
            console.log("hey " + num)
        }else{
            this.maxHeap.enqueue(num)
            console.log("MaxHeap " + this.maxHeap.front())
        }
        if(this.maxHeap.size() - 1 > this.minHeap.size()){
            let node = this.maxHeap.dequeue()
            this.minHeap.enqueue(node)
        }
    }

    /**
     * @return {number}
     */
    findMedian() {
        if(this.maxHeap.size() == this.minHeap.size()){
            return (this.maxHeap.front() + this.minHeap.front()) / 2
        }else{
            return this.maxHeap.front()
        }
    }
}
