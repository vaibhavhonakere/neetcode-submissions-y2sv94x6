class DSU{
    constructor(n){
        this.parent = Array.from({length: n}, (_,i) => i)
        this.rank = Array(n).fill(1);
    }
    find(node){
        let curr = node
        while(this.parent[curr] !== curr){
            this.parent[curr] = this.parent[this.parent[curr]]
            curr = this.parent[curr]
        }
        return curr
    }
    union(p1, p2){
        let first = this.find(p1)
        let second = this.find(p2)
        if(first === second){
            return 0
        }
        if(this.rank[first] > this.rank[second]){
            this.rank[first] += this.rank[second]
            this.parent[second] = first
        }else{
            this.rank[second] += this.rank[first]
            this.parent[first] = second
        }
        return 1
    }
}
// class DSU {
//     /**
//      * @param {number} n
//      */
//     constructor(n) {
//         this.parent = Array.from({ length: n }, (_, i) => i);
//         this.rank = Array(n).fill(1);
//     }

//     /**
//      * @param {number} node
//      * @return {number}
//      */
//     find(node) {
//         let cur = node;
//         while (cur !== this.parent[cur]) {
//             this.parent[cur] = this.parent[this.parent[cur]];
//             cur = this.parent[cur];
//         }
//         return cur;
//     }

//     /**
//      * @param {number} u
//      * @param {number} v
//      * @return {boolean}
//      */
//     union(u, v) {
//         let pu = this.find(u);
//         let pv = this.find(v);
//         if (pu === pv) {
//             return false;
//         }
//         if (this.rank[pv] > this.rank[pu]) {
//             [pu, pv] = [pv, pu];
//         }
//         this.parent[pv] = pu;
//         this.rank[pu] += this.rank[pv];
//         return true;
//     }
// }

class Solution {
    /**
     * @param {number[][]} edges
     * @return {number[]}
     */
    findRedundantConnection(edges) {
        let obj = new DSU(edges.length)
        for(let [p1,p2] of edges){
            if(!obj.union(p1,p2)){
                return [p1,p2]
            }
        }
        return []
    }
}
