/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSymmetric(TreeNode l, TreeNode r){
        if(l==null && r ==null) return true;
        else if(l==null || r==null) return false;
        else if(l.val!=r.val) return false;
        else {
            return isSymmetric(l.right, r.left) && isSymmetric(l.left, r.right);
        }
    }
    public boolean isSymmetric(TreeNode root) {
        return isSymmetric(root.left, root.right);
    }
}