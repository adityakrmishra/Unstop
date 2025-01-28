#include <iostream>
#include <vector>

using namespace std;

vector<int> findFlowersIndexes(int N, int t, vector<int>& a) {
    int left = 0, right = N - 1;
    vector<int> result;

    while (left < right) {
        int sum = a[left] + a[right];
        if (sum == t) {
            result.push_back(left);
            result.push_back(right);
            break;
        } else if (sum < t) {
            left++;
        } else {
            right--;
        }
    }

    return result;
}

int main() {
    int N, t;
    cin >> N >> t;

    vector<int> a(N);
    for (int i = 0; i < N; i++) {
        cin >> a[i];
    }

    vector<int> result = findFlowersIndexes(N, t, a);

    cout << result[0] << " " << result[1] << endl;

    return 0;
}
