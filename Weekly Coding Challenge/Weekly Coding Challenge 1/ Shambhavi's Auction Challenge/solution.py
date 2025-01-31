# Enter your code here. Read input from STDIN. Print output to STDOUT
import bisect

def manage_auction(N, M, artifact_prices, budgets):
    # Sort the artifact prices
    artifact_prices.sort()
    
    # Set to keep track of used artifacts
    used = set()
    
    # Result to store the output for each enthusiast
    result = []
    
    for budget in budgets:
        # Binary search to find the largest artifact price <= budget
        pos = bisect.bisect_right(artifact_prices, budget)
        
        if pos == 0:
            # No artifact can be bought because all are too expensive
            result.append(-1)
        else:
            # The largest possible artifact that fits within the budget
            chosen_price = artifact_prices[pos - 1]
            
            # Check if this artifact has already been used
            while chosen_price in used and pos > 0:
                pos -= 1
                if pos == 0:
                    chosen_price = -1
                    break
                chosen_price = artifact_prices[pos - 1]
            
            if chosen_price != -1:
                # Mark the artifact as used
                used.add(chosen_price)
                result.append(chosen_price)
            else:
                # No valid artifact can be bought
                result.append(-1)
    
    return result

# Input parsing
N, M = map(int, input().split())
artifact_prices = list(map(int, input().split()))
budgets = list(map(int, input().split()))

# Output the results
results = manage_auction(N, M, artifact_prices, budgets)
for res in results:
    print(res)
