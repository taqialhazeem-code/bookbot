def number_of_words(text):
        words = text.split()
        return len(words)
def number_of_characters(text):
        dict_chars = {}
        for char in text:
                if char.isalpha():
                        char = char.lower()
                        if char in dict_chars:
                                dict_chars[char] += 1
                        else:
                                dict_chars[char] = 1
        return dict_chars
def sorted_list_of_dictionaries(dict_chars):
        sorted_list = sorted(dict_chars.items(), key=lambda item: item[1], reverse=True)
        return sorted_list