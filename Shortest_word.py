def find_short(s):
    l = s.split()
    shortest_word = float('inf')
    for i in l:
        if len(i) < shortest_word:
            shortest_word = len(i)
    return shortest_word
