class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numberMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (numberMap.containsKey(complement)) {
                return new int[] { numberMap.get(complement), i };
            }
            numberMap.put(nums[i], i);
        }
        return null; 
    }
}