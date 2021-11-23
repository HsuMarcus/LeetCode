/*
 * @lc app=leetcode id=1 lang=cpp
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //sort(nums.begin(),nums.end());
        vector<int> result(2);
        unordered_map<int, int> hash;
        for(int i = 0; i < nums.size(); i++){
            int compliment = target - nums[i];
            if(hash.find(compliment) != hash.end()){
                    result[0] = hash.find(compliment)->second;
                    result[1] = i;
                    return result;
            }
            hash[nums[i]] = i;
        }
        return result;
    }     
};
// @lc code=end

