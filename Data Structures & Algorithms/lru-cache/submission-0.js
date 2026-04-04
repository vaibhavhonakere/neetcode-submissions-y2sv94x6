 class Node {
     constructor(key, val) {
         this.key = key;
         this.val = val;
         this.prev = null;
         this.next = null;
     }
 }
class LRUCache {
    /**
     * @param {number} capacity
     */
    constructor(capacity) {
        this.capacity = capacity
        this.front = new Node(0,0)
        this.back = new Node(0,0)
        this.cache = new Map()
        this.front.next = this.back;
        this.back.prev = this.front;
    }

    remove(node){
        let tmp = node.next
        let tmp2 = node.prev
        tmp2.next = tmp
        tmp.prev = tmp2

    }
    add(node){
        const nxt = this.front.next;
        nxt.prev = node;
        node.next = nxt;
        node.prev = this.front;
        this.front.next = node;

        // let tmp = this.front.next.next
        // this.front.next = node
        // node.prev = this.front
        // node.next = tmp
        // let deleteNode = this.front.next
        // remove(deleteNode)
    }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key) {
        if(this.cache.has(key) == false){
            return -1
        }
        let node = this.cache.get(key);
        let ret = node.val
        this.remove(node)
        this.add(node)
        return ret
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key, value) {
        if (this.cache.has(key)) {
            this.remove(this.cache.get(key));
        }
        let node = new Node(key, value)
        this.cache.set(key, node)
        this.add(node)
        if(this.cache.size > this.capacity){
            let lru = this.back.prev
            this.remove(lru)
            this.cache.delete(lru.key)
        }
        console.log(this.cache)
    }
}
