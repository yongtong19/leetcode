#include <string>
#include <iostream>
using namespace std;

class Solution
{
public:
    int scoreOfString(string s)
    {
        int ans = 0;

        for (int i = 1; i < s.size(); i++)
        {
            ans += abs(s.at(i) - s.at(i - 1));
        }

        return ans;
    }
};

int main()
{
    Solution s;
    cout << (s.scoreOfString("hello")) << endl;
}