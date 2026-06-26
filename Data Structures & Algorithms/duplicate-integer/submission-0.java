class Solution {
    public boolean hasDuplicate(int[] nums) {

        HashMap<Integer, Integer> hasmap = new HashMap<>();

        for(int i=0; i<nums.length; i++){
            if(hasmap.containsKey(nums[i])){
                return true;
            }
            hasmap.put(nums[i],nums[i]);
        }
        return false;
 
    }
}
