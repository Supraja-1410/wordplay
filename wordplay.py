# wordplay.py
# Program to process a word list and answer given tasks

def load_words(filename="wordlist.txt"):
    """Load words from a file into a list."""
    with open(filename, "r") as f:
        return [w.strip().lower() for w in f.readlines() if w.strip()]


def words_ending_with(words, suffix="ime"):
    return [w for w in words if w.endswith(suffix)]


def words_with_letters(words, letters="rstlne"):
    return [w for w in words if any(ch in w for ch in letters)]


def words_without_vowels(words):
    vowels = "aeiou"
    return [w for w in words if all(v not in w for v in vowels)]


def words_with_all_vowels(words):
    vowels = "aeiou"
    return [w for w in words if all(v in w for v in vowels)]


def compare_word_lengths(words, len1=10, len2=7):
    count1 = sum(1 for w in words if len(w) == len1)
    count2 = sum(1 for w in words if len(w) == len2)
    if count1 > count2:
        return f"More {len1}-letter words ({count1}) than {len2}-letter words ({count2})"
    elif count2 > count1:
        return f"More {len2}-letter words ({count2}) than {len1}-letter words ({count1})"
    else:
        return f"Equal number of {len1}-letter and {len2}-letter words ({count1} each)"


def longest_word(words):
    max_len = max(len(w) for w in words)
    return [w for w in words if len(w) == max_len]


def palindromes(words):
    return [w for w in words if w == w[::-1] and len(w) > 1]


def two_letter_words(words):
    return [w for w in words if len(w) == 2]


def main():
    words = load_words()

    print("a) Words ending in 'ime':", words_ending_with(words))
    print("b) Words with at least one of {r,s,t,l,n,e}: Count =", len(words_with_letters(words)))
    print("c) Words with no vowels:", words_without_vowels(words))
    print("d) Words containing all vowels:", words_with_all_vowels(words))
    print("e)", compare_word_lengths(words))
    print("f) Longest word(s):", longest_word(words))
    print("g) Palindromes:", palindromes(words))
    print("h) Two-letter words:", two_letter_words(words))


if __name__ == "__main__":
    main()
