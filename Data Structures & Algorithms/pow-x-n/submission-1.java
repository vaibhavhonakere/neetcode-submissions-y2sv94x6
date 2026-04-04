class Solution {
    private double base;
    public double myPow(double x, int n) {
        this.base = x;
        return dfs(n);
    }
    private double dfs(int n){
        if(n == 0){
            return 1.0;
        }
        if(n == -1){
            return (1/(this.base));
        }
        if(n == 1){
            return this.base;
        }
        int val = (int) (n/2);
        if(n % 2 == 0){
            return Math.pow(dfs(val), 2.0);
        }else{
            double tmp = 0;
            if(n < 0){
                tmp = (1/(this.base));
            }else{
                tmp = this.base;
            }
            return (Math.pow(dfs(val), 2.0) * tmp);
        }
    }
}
