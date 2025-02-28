#include <iostream>
#include <unordered_map>
#include <climits>
#include<bits/stdc++.h>

using namespace std;

int findAbsDifference(const vector<pair<int, int>>& queries) {
    unordered_map<int, int> freq_map;

    // Process each query
    for (const auto& q : queries) {
        int A = q.first, B = q.second;
        freq_map[B] += A; // Update frequency of number B
    }

    int min_freq = INT_MAX, max_freq = INT_MIN;
    int min_num = INT_MAX, max_num = INT_MIN;

    // Identify min and max frequency numbers
    for (const auto& entry : freq_map) {
        int num = entry.first, freq = entry.second;

        if (freq > 0) {  // Consider only numbers appearing at least once
            if (freq < min_freq || (freq == min_freq && num < min_num)) {
                min_freq = freq;
                min_num = num;
            }

            if (freq > max_freq || (freq == max_freq && num > max_num)) {
                max_freq = freq;
                max_num = num;
            }
        }
    }
    return abs(max_num - min_num);
}

int main() {
    int n;
    cin>>n;
    vector<pair<int,int>> queries(n);
    for(int i=0;i<n;i++){
        int x,y;
        cin>>x>>y;
        queries[i] = {x,y};
    }
    cout << findAbsDifference(queries) << endl;
    return 0;
}
