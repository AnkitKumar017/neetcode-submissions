class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxP=0;
        int buy=prices[0];

        for(int i=0;i<prices.size();i++){
            maxP = max(maxP,prices[i]-buy);
            buy = min(buy,prices[i]);
        }

        return maxP;
        
    }
};
