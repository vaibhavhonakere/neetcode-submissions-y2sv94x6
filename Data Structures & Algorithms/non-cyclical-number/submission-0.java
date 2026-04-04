class Solution {
    public boolean isHappy(int n) {
        int slow = helper(n);
        int fast = helper(helper(n));

        while(slow != fast){
            slow = helper(slow);
            fast = helper(helper(fast));
        }
        return fast == 1;
    }
    private int helper(int n) {
        int output = 0;
        while (n != 0) {
            output += (n % 10) * (n % 10);
            n /= 10;
        }
        return output;
    }
}
