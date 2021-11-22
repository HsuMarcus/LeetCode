/*
 * @lc app=leetcode id=53 lang=cpp
 *
 * [53] Maximum Subarray
 */

// @lc code=start
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max = nums[0];
        int temp = 0;
        for(int i = 0; i < nums.size(); i++){
            for(int j = i; j < nums.size(); j++){
                temp = 0;
                for(int k = i; k <= j ;k++){
                    temp += nums[k];   
                }
                if(temp > max) max = temp; 
            }
        }
        return max; 
    }
};
// @lc code=end

