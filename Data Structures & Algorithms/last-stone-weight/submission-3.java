class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for(int s: stones){
            queue.add(-s);
        }
        while(queue.size() > 1){
            int first = queue.peek();
            queue.poll();
            int second = queue.peek();
            queue.poll();
            System.out.println("first : " + first + " Second : " + second);
            if(first == second){
                continue;
            }if(first < second){
                queue.add(first - second);
            }
        }
        if(queue.size() == 1){
            return Math.abs(queue.poll());
        }
        return 0;
    }
}
