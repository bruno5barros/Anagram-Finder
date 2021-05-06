def validate_words_are_anagram(word1, word2):
    """Compare if this two words are anagrams"""
    letter_counts = {}

    for letter in word1:
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1

    for letter in word2:
        if not letter_counts[letter]:
            return False
        else:
            letter_counts[letter] -= 1

    return True


def find_anagrams(words):
    """Iterate the list and find anagrams"""
    anagrams_dict = {}
    for index, word in enumerate(words):
        for i in range(index + 1, len(words)):
            if len(word) == len(words[i]) and words[i] not in anagrams_dict:
                is_anagram = validate_words_are_anagram(word, words[i])
                if is_anagram:
                    if word not in anagrams_dict:
                        anagrams_dict[word] = word
                    if words[i] not in anagrams_dict:
                        anagrams_dict[words[i]] = word

    if len(anagrams_dict):
        res = ""
        bk_anagram = list(anagrams_dict)[0]
        for key, anagram in anagrams_dict.items():
            if bk_anagram == anagram:
                res += key + " "
            else:
                print(res)
                res = key + " "
                bk_anagram = anagram
        print(res)
    else:
        print("no anagrams found")


    return 0


words = []
try:
    with open("anagram.txt" , 'r') as f:
        lines = f.readlines()
        for line in lines:
            words += line.split()

        find_anagrams(words)
except IOError:
    print('There was an error opening the file!')
