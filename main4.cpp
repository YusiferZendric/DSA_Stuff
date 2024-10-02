//def req(nums):
//     if nums == sorted(nums):
//         return True
//     else:
//         for i in range(len(nums)):
//             newlist = nums[:i] + nums[i+1:]
//             if newlist == sorted(newlist):
//                 return True
//         else:
//             return False
// a = req([1,2,4,5,3])
// print(a)

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution{
    public:
        bool req(vector<int>& nums){
            if (is_sorted(nums.begin(), nums.end())){
                return true;
            } else{
                for (int i; i<nums.size(); i++){
                    vector<int> newList(nums.begin(), nums.end());
                    newList.erase(nums.begin()+i);
                    if (is_sorted(newList.begin(), newList.end())){
                        return true;
                    }
                }
                return false;

            }
        }
};

int main(){
    Solution solution;
    vector<int> nums1 = {1,5,2,15,25};
    cout << solution.req(nums1)<<endl;
    return 0;
}