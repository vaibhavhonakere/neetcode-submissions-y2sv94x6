class Solution {
    public int[] plusOne(int[] digits) {
        List<Integer> ret = new ArrayList<>();
        int carry = 1;
        for(int i = digits.length - 1; i >= 0; i--){
            int fullVal = digits[i] + carry;
            int actual = (int) (fullVal % 10);
            int rem = (int) (fullVal / 10);
            ret.add(actual);
            carry = rem;
            //System.out.println("The value " + fullVal + " actual " + actual + " rem " + rem);
        }
        if(carry > 0){
            ret.add(carry);
        }
        int[] res = new int[ret.size()];
        for(int j = ret.size() - 1; j >= 0 ; j--){
            res[(ret.size() - 1) - j] = ret.get(j);
        }
        return res;
    }
}
