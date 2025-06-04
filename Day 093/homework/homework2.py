def is_pangram(st):
    s = st.lower()
    for i in "qwertyuioplkjhgfdsazxcvbnm":
        if i not in s:
            return False
    return True
        