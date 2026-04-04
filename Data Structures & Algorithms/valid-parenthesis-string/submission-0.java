class Solution {
    public boolean checkValidString(String s) {
        int leftMin = 0;
        int leftMax = 0;
        for(Character let: s.toCharArray()){
            if(let == '('){
                leftMin += 1;
                leftMax += 1;
            }else if(let == ')'){
                leftMin -= 1;
                leftMax -= 1;
            }else if(let == '*'){
                leftMin -= 1;
                leftMax += 1;
            }
            if(leftMax < 0){
                return false;
            }
            if(leftMin < 0){
                leftMin = 0;
            }
        }
        return (leftMin == 0);
    }
}
