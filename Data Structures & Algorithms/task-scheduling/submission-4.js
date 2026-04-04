class Solution {
    /**
     * @param {character[]} tasks
     * @param {number} n
     * @return {number}
     */
    leastInterval(tasks, n) {
        const maxHeap = new MaxPriorityQueue(point => point[0])
        const cache = new Map()
        for(let t of tasks){
            if(cache.has(t)){
                cache.set(t, cache.get(t) + 1)
            }else{
                cache.set(t, 1)
            }
        }
        for(let [key, value] of cache){
            maxHeap.enqueue([value, key])
        }
        let time = 0
        let queue = []
        while(queue.length > 0 || maxHeap.size() > 0){
            if(maxHeap.size() > 0){
                let node = maxHeap.dequeue()
                let num = node[0]
                let char = node[1]
                console.log(num, char)
                if(num - 1 != 0){
                    queue.push([time + n, char, num - 1])
                }
            }
            if(queue.length > 0 && queue[0][0] === time){
                let n = queue.shift();
                let char = n[1]
                let num = n[2]
                maxHeap.enqueue([num,char]) 
            }
            time += 1
        }
        return time
    }
}
