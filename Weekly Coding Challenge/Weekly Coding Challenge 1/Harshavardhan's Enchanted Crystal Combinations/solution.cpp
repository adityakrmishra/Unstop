#include <iostream>
#include <cmath>
using namespace std;

// Function to count valid combinations
long long countCombinations(int N) {
    long long count = 0;

        // Iterate over 'a'
            for (int a = 1; a * a * a <= N; ++a) {
                    // Iterate over 'b' starting from 'a'
                            for (int b = a; a * b * b <= N; ++b) {
                                        // Calculate maximum valid 'c'
                                                    int maxC = N / (a * b);
                                                                count += maxC - b + 1; // Add all valid 'c' values
                                                                        }
                                                                            }

                                                                                return count;
                                                                                }

                                                                                int main() {
                                                                                    int N;
                                                                                        cin >> N; // Input the magical limit
                                                                                            cout << countCombinations(N) << endl; // Output the result
                                                                                                return 0;
                                                                                                }
