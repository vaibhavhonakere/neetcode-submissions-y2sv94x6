class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;
        int maxWater = -1;
        while(left < right){
            maxWater = Math.max(Math.min(heights[left], heights[right])*(right - left), maxWater);
            if(heights[left] < heights[right]){
                left++;
            }else{
                right--;
            }
        }
        return maxWater;
    }
}
