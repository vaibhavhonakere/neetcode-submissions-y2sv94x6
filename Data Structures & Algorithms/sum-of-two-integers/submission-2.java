class Solution {
    public int getSum(int a, int b) {
        while(b != 0){
            int temp_1 = a ^ b;
            int temp_2 = (a & b) << 1;
            a = temp_1;
            b = temp_2;
        }
        return a;
    }
}
