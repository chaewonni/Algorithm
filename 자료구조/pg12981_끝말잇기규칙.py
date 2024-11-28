def solution(n, words):
    use_word = set()
    prev_word = words[0][0]
    
    for i, word in enumerate(words):
        if word in use_word or word[0] != prev_word:
            return [(i % n) + 1, (i // n) + 1]
        use_word.add(word)
        prev_word = word[-1]
    return [0,0]