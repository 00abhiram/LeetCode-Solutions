class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxCount = 0;
        int currCount = 0;
        for(int num : nums){
            if(num == 1){
                currCount++;
                maxCount = Math.max(currCount , maxCount);
            }else{
                currCount = 0;
            }
        }
        return maxCount;
    }
}