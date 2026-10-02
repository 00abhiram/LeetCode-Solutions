class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> result = new ArrayList<>();
        if(nums == null || nums.length == 0) return result;
        int cand1 =0 , cand2 = 0;
        int count1 = 0 , count2 = 0;

        for(int num : nums){
            if(num == cand1){
                count1++;
            }else if(num == cand2){
                count2++;
            }else if(count1 == 0){
                cand1 = num;
                count1 = 1;
            }else if(count2 == 0){
                cand2 = num;
                count2 = 1;
            }else{
                count1--;
                count2--;
            }
        }
        count1 = 0;
        count2 = 0;
        for (int num : nums){
            if(num == cand1)count1++;
            else if (num == cand2) count2++;
        }
        int target = nums.length/3;
        if(count1 > target) result.add(cand1);
        if(count2 > target) result.add(cand2);
    return result;
    }
}