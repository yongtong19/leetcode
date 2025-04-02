#include <vector>
#include <iostream>
using namespace std;

class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {
        int i = 0;
        int j = nums.size() - 1;

        while (i < j)
        {
            while (i < j && nums[j] == val)
                j--;
            if (nums[i] == val)
            {
                swap(nums[i], nums[j]);
            }
            i++;
        }

        return j + 1;
    }
};

int main()
{
    Solution s;
    vector<int> nums{1};
    cout << s.removeElement(nums, 1) << endl;
    for (auto num : nums)
    {
        cout << num;
    }
    cout << endl;
}