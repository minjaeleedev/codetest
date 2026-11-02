public class Solution {
    /**
     * Approach 5. Without Finding Median
     */
    public int minMoves2(int[] nums) {
        int l = 0, r = nums.length - 1, sum = 0;
        Arrays.sort(nums);
        while (l < r) {
            sum += nums[r] - nums[l];
            l++;
            r--;
        }
        return sum;
    }
}