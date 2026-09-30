import java.util.HashSet;
import java.util.Set;
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0){
            return 0;
        }
        Set<Integer> numset = new HashSet<>();
        for (int num : nums){
            numset.add(num);
        }
        int Longeststreak = 0;
        for(int num : numset){
            if(!numset.contains(num-1)){
                int currnum = num;
                int currstreak = 1;
                while(numset.contains(currnum +1)){
                    currnum +=1;
                    currstreak +=1;
                }
                Longeststreak = Math.max(currstreak , Longeststreak);
            }
        }
        return Longeststreak;
    }
}