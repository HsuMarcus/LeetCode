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
            if((temp + nums[i]) > nums[i]) {
                temp += nums[i];
            }else{
                temp = nums[i];
            }

            if(temp > max){
                max = temp;
            }
        }
        return max; 
    }
};
// @lc code=end

