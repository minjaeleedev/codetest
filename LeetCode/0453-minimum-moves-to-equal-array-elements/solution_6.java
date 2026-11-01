public class Solution {
    /** 
    * Approach 6: Modified Approach Using Math
    * There could be a problem with the Approach 5. 
    * The value of the sum of nums[i] could be very large and hence could lead to integer overflow
    * if nums[i]'s are very large.
    * To avoid this problem, we can calculate the required number of `moves` on the fly.
    */
    public int minMoves(int[] nums) {
        int moves = 0, min = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length; i++) {
            min = Math.min(min, nums[i]);
        }
        for (int i = 0; i < nums.length; i++) {
            moves += nums[i] - min;
        }
        return moves;
    }
}