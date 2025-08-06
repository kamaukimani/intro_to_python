def first_non_repeating(s):
    s_lower = s.lower()
    for char in s:
        if s_lower.count(char.lower()) == 1:
            return char
    return None

print(first_non_repeating("Hello"))  # "H"
print(first_non_repeating("Swiss"))  # "w"