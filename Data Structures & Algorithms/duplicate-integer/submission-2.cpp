class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> seen;
        for (int num: nums) {
            if (!seen.contains(num)) {
                seen.emplace(num);
            }
            else {
                return true;
            }
        }
        return false;
    }
};