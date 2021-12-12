def naive_substring_matcher(string: str, substring: str):
    n = len(string)
    m = len(substring)
    for i in range(0, n - m + 1):
        if string[i:i + m] == substring:
            return i
    return None

if __name__ == '__main__':
    string = "lililosa lililacaba"
    substring = "lilila"
    print(naive_substring_matcher(string, substring))