class Solution {
    public int maxSubArray(int[] nums) {
        int maxSofar = nums[0];
        int currentMax = nums[0];
        for(int i = 1; i<nums.length; i++){
            currentMax = Math.max(nums[i],currentMax+nums[i]);
            maxSofar = Math.max(maxSofar , currentMax);
        }
        return maxSofar;
    }
}