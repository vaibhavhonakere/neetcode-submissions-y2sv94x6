class Solution {
    /**
     * @param {number} n
     * @param {number[][]} flights
     * @param {number} src
     * @param {number} dst
     * @param {number} k
     * @return {number}
     */
    findCheapestPrice(n, flights, src, dst, k) {
        // Adjacent Map
        // Have distance list
        const dist = Array(n).fill(Number.MAX_SAFE_INTEGER)
        dist[src] = 0
        const adjMap = new Map()
        for(let i = 0; i < n; i++){
            adjMap.set(i, []);
        }
        for(let [s, dst, cost] of flights){
            let newList = adjMap.get(s)
            newList.push([dst, cost])
            adjMap.set(s, newList)
        }
        let q = new Queue()
        q.enqueue([src, 0, 0])
        while(q.size() > 0){
            const [node,stop,prev] = q.dequeue()
            if(stop > k){
                continue
            }
            for(let [d, c] of adjMap.get(node)){
                let newVal = prev + c
                if(newVal < dist[d]){
                    dist[d] = newVal
                    q.enqueue([d, stop + 1, newVal])
                }
            }
        }
        return dist[dst] === Number.MAX_SAFE_INTEGER ? -1 : dist[dst]
    }
}
