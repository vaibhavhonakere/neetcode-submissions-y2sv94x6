class Pair {
    int freq;
    char task;
    int time;

    public Pair(int freq, char task, int time) {
        this.freq = freq;
        this.task = task;
        this.time = time;
    }
}

class Solution {
    public int leastInterval(char[] tasks, int n) {
        // // // Create a minHeap based on frequency
        // PriorityQueue<Pair> minHeap = new PriorityQueue<>(Comparator.comparing(p -> -p.freq)); // Max heap based on freq

        // // Count frequency of each task
        // HashMap<Character, Integer> let_To_Freq = new HashMap<>();
        // for (char c : tasks) {
        //     let_To_Freq.put(c, let_To_Freq.getOrDefault(c, 0) + 1);
        // }

        // // Add the tasks to the minHeap
        // for (Map.Entry<Character, Integer> entry : let_To_Freq.entrySet()) {
        //     minHeap.add(new Pair(entry.getValue(), entry.getKey(), 0));
        // }

        // // Queue to manage cooldown times
        // Queue<Pair> cooldownQueue = new LinkedList<>();
        // int time = 0;

        // // Loop until all tasks are processed
        // while (!minHeap.isEmpty() || !cooldownQueue.isEmpty()) {
        //     if (!minHeap.isEmpty()) {
        //         // Process the task with the highest frequency
        //         Pair currentTask = minHeap.poll();
        //         currentTask.freq += 1; // Decrease the frequency

        //         // Add task to cooldown if it still has remaining executions
        //         if (currentTask.freq > 0) {
        //             cooldownQueue.add(new Pair(currentTask.freq, currentTask.task, time + n));
        //         }
        //     }
        //     // Handle cooldowns: Re-add the task to the heap after cooldown is done
        //     if (!cooldownQueue.isEmpty() && cooldownQueue.peek().freq >= time) {
        //         minHeap.add(cooldownQueue.poll());
        //     }
        //     // Increment time
        //     time++;
        // }

        // return time + 1;
        // PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparing(a -> a[0]));
        // HashMap<Character, Integer> let_To_Freq = new HashMap<>();
        // for(char c: tasks){
        //     let_To_Freq.put(c, let_To_Freq.getOrDefault(c,0) + 1);
        // }
        // for(Map.Entry<Character,Integer> mapElement : let_To_Freq.entrySet()){
        //     Character c = mapElement.getKey();
        //     int value = mapElement.getValue();
        //     minHeap.add(new int[]{-1*value, (int)c});
        // }
        // Queue<int[]> q = new LinkedList<>();
        // int time = 0;
        // while(minHeap.size() > 0 || q.size() > 0){
        //     int value = 0;
        //     Character c = '0';
        //     if(minHeap.size() > 0){
        //         int[] pair = minHeap.poll(); // [value, Character]
        //         value = pair[0];
        //         c = (char) pair[1];
        //         q.add(new int[]{value + 1, (int)c, time + n});
        //     }
        //     if(q.size() > 0 && time == q.peek()[2]){
        //         int[] triplet = q.poll(); // [value, Character, time]
        //         minHeap.add(new int[]{triplet[0], triplet[1]});
        //     }
        //     time += 1;
        // }
        // return time + 1;
        // PriorityQueue that acts like a max-heap based on the first element (negative frequency)
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(p -> p[0]));

        // Count the frequency of each task
        HashMap<Character, Integer> let_To_Freq = new HashMap<>();
        for (char c : tasks) {
            let_To_Freq.put(c, let_To_Freq.getOrDefault(c, 0) + 1);
        }

        // Add the tasks to the minHeap as [-frequency, character]
        for (Map.Entry<Character, Integer> entry : let_To_Freq.entrySet()) {
            minHeap.add(new int[]{-entry.getValue(), entry.getKey()}); // Negative for max-heap effect
        }

        // Queue to manage cooldown
        Queue<int[]> cooldownQueue = new LinkedList<>();
        int time = 0;

        // Loop until all tasks are processed
        while (!minHeap.isEmpty() || !cooldownQueue.isEmpty()) {
            time++;

            // If the heap has tasks to process
            if (!minHeap.isEmpty()) {
                // Poll the task with the highest frequency
                int[] currentTask = minHeap.poll();
                currentTask[0]++; // Reduce frequency (since it's negative, increment towards 0)

                // If there are remaining instances of the task, add it to the cooldown
                if (currentTask[0] < 0) {
                    cooldownQueue.add(new int[]{currentTask[0], currentTask[1], time + n});
                }
            }

            // Check if any task in cooldown is ready to be added back to the heap
            if (!cooldownQueue.isEmpty() && cooldownQueue.peek()[2] == time) {
                minHeap.add(cooldownQueue.poll());
            }
        }

        return time;


    }   
}
