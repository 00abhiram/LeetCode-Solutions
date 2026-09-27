class Solution {
    public int majorityElement(int[] nums) {
        int candid = nums[0];
        int count = 0;
        for (int num : nums){
            if (count == 0){
                candid = num;
            }
            if ( num == candid){
                count++;
            }else{
                count--;
            }
        }
        return candid;
    }
}