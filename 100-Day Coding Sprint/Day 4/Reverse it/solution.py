def reverse_portion_naive(s, ch):
    # Find the last occurrence of 'ch'
    last_index = -1
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ch:
            last_index = i
            break

    if last_index == -1:
        return s  # Character not found

    # Reverse the portion from the last occurrence to the end
    return s[:last_index] + s[last_index:][::-1]

if __name__ == "__main__":
    line = input().strip()
    s, ch = line.split()
    print(reverse_portion_naive(s, ch))
