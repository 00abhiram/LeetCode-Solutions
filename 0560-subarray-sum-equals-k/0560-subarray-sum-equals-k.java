import java.util.HashMap;
class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        int currSum = 0;
        HashMap<Integer , Integer> prefixSumMap = new HashMap<>();
        prefixSumMap.put(0,1);
        for (int num : nums){
            currSum += num;
            if(prefixSumMap.containsKey(currSum -k)){
                count += prefixSumMap.get(currSum -k);
            }
            prefixSumMap.put(currSum,prefixSumMap.getOrDefault(currSum,0)+1);
        }
        return count;
    }
}