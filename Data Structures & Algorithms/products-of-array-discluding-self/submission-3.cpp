class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {

        int n = nums.size();
        vector<int>arr(n);

        int pre = 1;
        int post = 1;

        for(int i=0;i<n;i++){
            arr[i] = pre;
            pre = nums[i]*pre;
        }

        for(int j=n-1;j>=0;j--){
            arr[j] = post*arr[j];
            post = post*nums[j];
        }

        return arr;

    }
};
