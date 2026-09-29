class Solution {
    public int[] rearrangeArray(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        int posIdx = 0;
        int negIdx = 1;
        for(int num : nums){
            if (num > 0){
                result[posIdx] = num;
                posIdx += 2;
            }else{
                result[negIdx] = num;
                negIdx += 2;
            }
        }
        return result;
    }
}