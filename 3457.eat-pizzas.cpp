class Solution {
public:
    long long maxWeight(vector<int>& pizzas) {
        sort(pizzas.begin(), pizzas.end());
        long long totalGain = 0;
        int n = pizzas.size();
        for (int i = 0; i < n; i += 4) {
            int Z = pizzas[i + 3]; // Largest of four
            int Y = pizzas[i + 2]; // Second largest of four
            // Odd-indexed day (1-indexed), gain Z weight
            if ((i / 4) % 2 == 0) {
                totalGain += Z;
            } else { // Even-indexed day (1-indexed), gain Y weight
                totalGain += Y;
            }
        }
        return totalGain;
    }
};