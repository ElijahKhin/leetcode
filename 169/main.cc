#include <iostream>
#include <map>

class Solution {
public:
  int majorityElement(std::vector<int>& nums) {
    for (auto& i : nums) {
      ++m[i];
    }
    auto it = find_if(m.begin(), m.end(), [this, &nums] (const std::pair<int, int> el) {return el.second > nums.size() /  2;});
    return it->first;
  }

private:
  std::map<int, int> m;
};

int main() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  
  std::vector<int> nums = {2,2,1,1,1,2,2};
  Solution sol;
  int val = sol.majorityElement(nums);
  std::cout << val << '\n';
}
