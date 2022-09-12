class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> pairs = new HashMap<Integer, Integer>();
        
        for(int i = 0; i < nums.length; i++) {
            int compliment = target - nums[i];
            if (pairs.containsKey(compliment)) {
                return new int[]{i, pairs.get(compliment)};
            }
            pairs.put(nums[i], i);
        }
        return new int[2];
    }
    
}

// public int[] twoSum(int[] nums, int target) {
//         HashMap<Integer, Integer> tracker = new HashMap<Integer, Integer>();
//         int len = nums.length;
//         for(int i = 0; i < len; i++){
//             if(tracker.containsKey(nums[i])){
//                 int left = tracker.get(nums[i]);
//                 return new int[]{left+1, i+1};
//             }else{
//                 tracker.put(target - nums[i], i);
//             }
//         }
//         return new int[2];
//     }