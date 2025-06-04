def duplicate_count(text):
    low = text.lower()
    dup = []
    for letter in low:
        if low.count(letter) > 1 and letter not in dup:
            dup.append(letter)
    return len(dup)
    
     