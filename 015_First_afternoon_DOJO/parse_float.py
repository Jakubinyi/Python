def parse_float(string):
    if string.isalpha():
        result = None
    else:
        result = float(string)
    return result

# Test:
print(parse_float("1.0"))
print(parse_float("a"))
print(parse_float("234.0234"))
print(parse_float("2"))
