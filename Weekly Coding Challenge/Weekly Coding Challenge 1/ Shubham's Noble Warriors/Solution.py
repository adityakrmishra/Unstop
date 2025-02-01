# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

def count_valid_teams(N, K, strengths):
    valid_team_count = 0
    
    # Generate all possible subsets using combinations
    # Check all subsets of all possible sizes (1 to N)
    for r in range(1, N + 1):
        for combo in combinations(strengths, r):
            # Check if this subset is valid
            is_valid = True
            for i in range(r):
                for j in range(i + 1, r):
                    if abs(combo[i] - combo[j]) == K:
                        is_valid = False
                        break
                if not is_valid:
                    break
            if is_valid:
                valid_team_count += 1
                
    return valid_team_count

# Input handling
N, K = map(int, input().split())  # Read N and K
strengths = list(map(int, input().split()))  # Read the strengths of knights
result = count_valid_teams(N, K, strengths)  # Calculate the number of valid teams
print(result)  # Output the result
