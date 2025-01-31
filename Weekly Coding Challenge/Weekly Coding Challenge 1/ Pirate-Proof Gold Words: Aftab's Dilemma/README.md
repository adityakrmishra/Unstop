# Problem Statement
Aftab has received several boxes filled with gold that need to be protected from pirates.

These boxes are lined up in such a way that they form a message, with a single letter written on each box. To ensure the safety of the gold, Aftab decides to create distinct messages by separating any two consecutive boxes at a time.

He wants to know how many distinct messages he can form by doing this, so he can send the list to the ship's captain and avoid an attack by the pirates.

Note: The boxes consists of only lowercase letters.

## Input Format
The first and only line of input holds a single string, message consisting of lowercase letters.

## Output Format
Print an integer representing the number of distinct messages that can be formed.

## Constraints
The length of the string message will be at most 10^5.

## Sample Testcase 0
### Testcase Input
aabb
### Testcase Output
3
## Explanation

Removing 'aa' results in "bb".

Removing 'ab' results in "ab".

Removing 'bb' results in "aa".


Thus, the distinct words are "ab", "bb" and "aa".

## Sample Testcase 1
### Testcase Input
abcd
### Testcase Output
3
## Explanation

Removing 'ab' results in "cd".

Removing 'bc' results in "ad".

Removing 'cd' results in "ab".


Thus, the distinct messages are "cd", "ad", and "ab".
