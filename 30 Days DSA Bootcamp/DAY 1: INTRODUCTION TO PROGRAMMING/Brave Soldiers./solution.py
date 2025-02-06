def count_brave_soldiers(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for num in range(2, n + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, n + 1, num):
                is_prime[multiple] = False
    return len(primes)
    
n=int(input())
print(count_brave_soldiers(n))
