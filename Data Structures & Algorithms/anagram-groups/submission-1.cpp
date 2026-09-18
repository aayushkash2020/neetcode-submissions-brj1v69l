class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<array<int, 26>, vector<string>> groups;
        for (const auto& str: strs) {
            array<int, 26> count{};
            for (char c: str) {
                count[c - 'a']++;
            }
            groups[count].push_back(str);
        }
        vector<vector<string>> result;
        for (auto& pair: groups) {
            result.push_back(std::move(pair.second));
        }
        return result;
    }
};
