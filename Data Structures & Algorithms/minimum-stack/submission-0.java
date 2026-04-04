class MinStack {
    Stack<Integer> min;
    Stack<Integer> normal;

    public MinStack() {
        this.min = new Stack<>();
        this.normal = new Stack<>();
    }
    
    public void push(int val) {
        if(!min.isEmpty()){
            int min_val = Math.min(min.peek(), val);
            min.push(min_val);
        }else{
            min.push(val);
        }
        normal.push(val);
    }
    
    public void pop() {
        min.pop();
        normal.pop();
    }
    
    public int top() {
        return normal.peek();
    }
    
    public int getMin() {
        return min.peek();
    }
}
