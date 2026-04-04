class Solution {
    public String multiply(String num1, String num2) {
        if(num1.equals("0") || num2.equals("0")){
            return "0";
        }
        int[] ret = new int[num1.length() + num2.length()];
        num1 = new StringBuilder(num1).reverse().toString();
        num2 = new StringBuilder(num2).reverse().toString();

        for(int i=0; i < num1.length(); i++){
            for(int j=0; j < num2.length(); j++){
                int first = Character.getNumericValue(num1.charAt(i));
                int second = Character.getNumericValue(num2.charAt(j));
                int digits = (first * second);

                ret[i + j] += digits;
                ret[i + j + 1] += ret[i + j] / 10;
                ret[i + j] %= 10;
            }
        }

        int last = ret.length - 1;
        while(last >= 0 && ret[last] == 0){
            last--;
        }
        StringBuilder s = new StringBuilder();
        for(int j = last; j >= 0; j--){
            s.append(ret[j]);
        }
        return s.toString();
    }
}
