class MedianFinder {
    private PriorityQueue<Integer> minHeap;
    private PriorityQueue<Integer> maxHeap;

    public MedianFinder() {
        this.minHeap = new PriorityQueue<>();
        this.maxHeap = new PriorityQueue<>();
    }
    private void addMaxHeap(){
        if(minHeap.size() > maxHeap.size() + 1){
            int val = minHeap.poll(); // minimum value in the heap
            maxHeap.offer(-1*val);
        }
    }
    private void addMinHeap(){
        if(maxHeap.size() > minHeap.size() + 1){
            int val = maxHeap.poll(); // minimum value in the heap
            minHeap.offer(-1*val);
        }
    }
    
    public void addNum(int num) {
        maxHeap.offer(-1 * num);
        addMinHeap();
        // System.out.println("MinHeap : " + minHeap.peek());
        // System.out.println("MaxHeap : " + maxHeap.peek());
        if(!minHeap.isEmpty() && !maxHeap.isEmpty() && (-1)*maxHeap.peek() > minHeap.peek()){
            int val = -1 * maxHeap.poll();
            minHeap.offer(val);
            val = minHeap.poll();
            maxHeap.offer(-1*val);
        }
    }
    public double findMedian() {
        if(maxHeap.size() > minHeap.size()){
            return (double) (-1 * maxHeap.peek());
        }else if(maxHeap.size() < minHeap.size()){
            return (double) (minHeap.peek());
        }else{
            // System.out.println("MinHeap : " + minHeap.peek());
            // System.out.println("MaxHeap : " + -1 * maxHeap.peek());
            // System.out.println("The sum : " + maxHeap.peek());
            int first = -1 *maxHeap.peek();
            int second = minHeap.peek();
            return (double) ((first + second) / (2.0));
        }
    }
}
