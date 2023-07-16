class RussianLatiniser:
    alphabet = {"а": "a",
                "б": "b",
                "в": "w",
                "г": "g",
                "д": "d",
                "е": "ê",
                "ё": "ô",
                "ж": "ž",
                "з": "z",
                "и": "i",
                "й": "j",
                "к": "k",
                "л": "l",
                "м": "m",
                "н": "n",
                "о": "o",
                "п": "p",
                "р": "r",
                "с": "s",
                "т": "t",
                "у": "u",
                "ф": "f",
                "х": "h",
                "ц": "c",
                "ч": "č",
                "ш": "š",
                "щ": "ŝ",
                "ъ": "j",
                "ы": "y",
                "ь": "j",
                "э": "e",
                "ю": "û",
                "я": "â"}

    compound_vowels_cyrillic = {
        "я": "a",
        "е": "e",
        "ё": "o",
        "ю": "u"}

    compound_vowels_latin = {
        "â": "a",
        "ê": "e",
        "ô": "o",
        "û": "u"}

    base_vowels = ["a", "i", "o", "e", "u", "y"]

    special_combinations = {
        "ться": "ca",
        "тся": "ca",
    }

    digraphs = {"йе": "je",
                "йё": "jo",
                "йю": "ju",
                "йя": "ja",
                "ше": "še",
                "шё": "šo",
                "шю": "šu",
                "шя": "ša",
                "ши": "šy",
                "ще": "ŝe",
                "щё": "ŝo",
                "щю": "ŝu",
                "щя": "ŝa",
                "че": "če",
                "чё": "čo",
                "чю": "ču",
                "чя": "ča",
                "це": "ce",
                "цё": "co",
                "цю": "cu",
                "ця": "ca",
                "же": "že",
                "жё": "žo",
                "жю": "žu",
                "жя": "ža",
                "жи": "žy",
                "ъя": "ja",
                "ъе": "je",
                "ъё": "jo",
                "ъи": "ji",
                "ьи": "jî",
                "ъю": "ju",
                "/n": "\n"}

    merged_vowels_list = base_vowels + list(compound_vowels_latin.keys())

    def __init__(self):
        pass

    # region utility
    @staticmethod
    def _insert(source_str, insert_str, pos):
        return source_str[:pos] + insert_str + source_str[pos:]

    @staticmethod
    def _extend_base_word(base_word, extension_position=1):
        word_len = len(base_word)
        if extension_position <= 0:
            extension_position = -1

        if extension_position >= word_len - 1:
            return base_word + base_word[-1]
        else:
            return base_word[:extension_position] + base_word[extension_position] + base_word[extension_position:]

    @staticmethod
    def _find_all_occurrences(main_string, substring):
        occurrences = []
        start_index = 0

        while True:
            index = main_string.find(substring, start_index)
            if index == -1:
                break
            occurrences.append(index)
            start_index = index + 1

        return occurrences

    # endregion

    def _transliterate_word(self, base_word):
        res = ""
        modified_word = base_word.lower()
        first_letter = base_word[0].lower()

        if len(base_word) > 0:
            # Process the first compound letter
            if first_letter in self.compound_vowels_cyrillic.keys():
                modified_word = "j" + self.compound_vowels_cyrillic[first_letter] + modified_word[1:]
                base_word = self._extend_base_word(base_word)

            for dig_st in range(len(modified_word) - 1):
                digraph = modified_word[dig_st:dig_st + 2]
                if digraph in self.digraphs.keys():
                    modified_word = modified_word.replace(digraph, self.digraphs[digraph])
                    continue

            # replace special combinations
            for combination in self.special_combinations.keys():
                occurrences = self._find_all_occurrences(modified_word, combination)
                new_combination = self.special_combinations[combination]
                new_combination_len = len(new_combination)
                modified_word = modified_word.replace(combination, new_combination)

                for occurrence in occurrences:
                    base_word = base_word[:occurrence] + base_word[occurrence + new_combination_len:]

            # replace common letters
            for letter in set(modified_word):
                if letter in self.alphabet.keys():
                    modified_word = modified_word.replace(letter, self.alphabet[letter])

            # Generate separated vowels
            word_len_counter = 1
            while word_len_counter != len(modified_word):
                cur_letter = modified_word[word_len_counter]
                if cur_letter in self.compound_vowels_latin.keys() and modified_word[
                    word_len_counter - 1] in self.merged_vowels_list:
                    modified_word = modified_word.replace(cur_letter, self.compound_vowels_latin[cur_letter], 1)
                    modified_word = self._insert(modified_word, "j", word_len_counter)
                    base_word = self._extend_base_word(base_word, word_len_counter)
                word_len_counter += 1

            # Set capital letters
            for char_a, char_b in zip(base_word, modified_word):
                if char_a.isupper():
                    res += char_b.upper()
                else:
                    res += char_b.lower()

        return res

    def transliterate_cyrillics_to_latin(self, text):
        word_list = text.split(" ")

        for word in range(0, len(word_list)):
            word_list[word] = self._transliterate_word(word_list[word])

        return ' '.join(word_list)


print(RussianLatiniser().transliterate_cyrillics_to_latin("Таллин - рига, поезд"))
