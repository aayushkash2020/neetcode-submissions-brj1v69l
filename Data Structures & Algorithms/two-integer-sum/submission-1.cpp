class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> num_to_idx;
        for (int i=0; i < nums.size(); i++) {
            auto it = num_to_idx.find(target - nums[i]);
            if (it != num_to_idx.end()) {
                return {it->second, i};
            }
            num_to_idx[nums[i]] = i;
        }
        return {-1, -1};
    }
};
