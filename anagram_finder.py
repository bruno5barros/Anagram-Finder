def validate_words_are_anagram(word1, word2):
    letter_counts = {}

    for letter in word1:
        #print(letter)
        if letter not in letter_counts:
            letter_counts[letter] = 1
        else:
            letter_counts[letter] += 1

    for letter in word2:
        #print(letter)
        if not letter_counts[letter]:
            return False
        else:
            letter_counts[letter] -= 1

    return True


def find_anagrams(words):
    #print(type(words))
    #words.sort()
    #print(words)
    anagrams_dict = {}
    for index, word in enumerate(words):
        #print(index, word)
        for i in range(index + 1, len(words)):
            #print(f"Next word in position: {i}, {words[i]}, {len(word) == len(words[i]), {word not in anagrams_dict}}")
            if len(word) == len(words[i]) and words[i] not in anagrams_dict:
                is_anagram = validate_words_are_anagram(word, words[i])
                if is_anagram:
                    if word not in anagrams_dict:
                        anagrams_dict[word] = word
                    if words[i] not in anagrams_dict:
                        anagrams_dict[words[i]] = word

    #print(anagrams_dict)
    if len(anagrams_dict):
        res = ""
        bk_anagram = list(anagrams_dict)[0]
        for key, anagram in anagrams_dict.items():
            #print(f"bk anagram: {bk_anagram}")
            #print(f"anagram: {anagram}")
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
        #print(lines)
        for line in lines:
            words += line.split()

        #print(words)
        find_anagrams(words)
except IOError:
    print('There was an error opening the file!')
