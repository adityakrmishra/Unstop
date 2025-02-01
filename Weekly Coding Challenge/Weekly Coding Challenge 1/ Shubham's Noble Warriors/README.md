# Problem Statement
In the legendary kingdom of Camelot, the wise King Shubham gathered a brave group of knights to prepare for a fierce battle against a menacing dragon. Each knight possesses a unique strength, symbolized by positive integers that glimmer like stars in the night sky. As they assembled, Shubham faced a critical decision: how to form a team of knights strong enough to defeat the dragon without creating conflicts among them.

The king laid down a crucial rule: no two knights in the same team could have a strength difference of exactly ( K ). This condition ensured harmony among the knights, preventing any quarrels that might weaken their resolve in the face of danger. 

As the knights stood ready, Shubham sought your assistance in counting how many different "Warrior" teams could be formed from the strengths of his knights. With their unique strengths at your disposal, your task is to explore all possible combinations and find the number of valid teams that maintain the king's rule.

## Input Format
The first line contains two space separated integers N and K representing the number of knights and the forbidden strength difference respectively.

The second line contains N integers separated by spaces, representing the strengths of the knights.

## Output Format
Print a single integer, the number of different Warrior teams that can be formed.

## Constraints
1 <= N <= 10^2

1 <= K <= 10^5

1 <= Strength of each knight <= 10^7

#### Sample Testcase 0
#####Testcase Input
5 2
1 3 5 7 9
#####Testcase Output
12
## Explanation
The Warrior team of Knights are:


Singles: {1}, {3}, {5}, {7}, {9}
Pairs: {1,5}; {1,7}; {1,9}; {3,7}; {3,9}; {5,9}
Triplets: {1,5,9}


Total "Warrior" Teams: 5 + 6 + 1 = 12.

### Sample Testcase 1
#### Testcase Input
3 2
2 4 6
#### Testcase Output
4
## Explanation
The "Warrior" teams of the knights are: 
{2}, {4}, {6}, {2, 6}.
Only 4 beautiful teams that can be formed from the knights [2,4,6].
