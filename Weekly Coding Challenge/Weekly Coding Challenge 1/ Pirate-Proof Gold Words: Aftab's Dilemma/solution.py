def count_distinct_words_by_removing_pairs(word):
    distinct_words=set()
    for i in range(len(word) - 1):
        new_word=word[:i]+word[i+2:]
        distinct_words.add(new_word)
    return len(distinct_words)

word=input().strip()
print(count_distinct_words_by_removing_pairs(word))
