import re
import string


class TextConvert:
    def __init__(self, txt_file):
        self.txt_file = txt_file

        self.capital_dict = {}
        self.pig_list = []

    def translate_word(self, word):
        vowels = ["a", "e", "i", "o", "u"]
        if word[0] in vowels:
            return word + "yay"

        for i in range(len(word)):
            if word[i] in vowels:
                return word[i:] + word[:i] + "ay"

        return word + "ay"  # No vowels found

    def get_text(self):
        with open(self.txt_file, "r") as txt_file:
            output = txt_file.read()

        # Updated regex to capture words separately from punctuation
        regex_pattern = r"(\b[\w'-]+)([.,!?;]?)"
        individual_words = re.findall(regex_pattern, output)
        # Construct final result by appending word and punctuation
        list_of_words_and_punct = [
            word + punctuation for word, punctuation in individual_words
        ]

        # print(list_of_words_and_punct)
        return list_of_words_and_punct

    def convert_words(self):
        lsit_of_words = self.get_text()

        for word in lsit_of_words:
            # handles word that is upper case and also ends with punctuation.
            if word[0].isupper() and word.endswith(tuple(string.punctuation)):
                punctuation = word[-1]  # store punctuation
                word = word[:-1]  # remove punctuation
                word = word.lower()
                pig_word = self.translate_word(word)
                pig_word = pig_word[0].upper() + pig_word[1:]
                # print (pig_word + punctuation)
                self.pig_list.append(pig_word + punctuation)
            # handels upper case words
            elif word[0].isupper():
                word = word.lower()
                pig_word = self.translate_word(word)
                pig_word = pig_word[0].upper() + pig_word[1:]

                # print(pig_word)
                self.pig_list.append(pig_word)
            # handles lower case words with punctuation
            elif word.endswith(tuple(string.punctuation)):
                punctuation = word[-1]  # store punctuation
                word = word[:-1]  # remove punctuation
                word = word.lower()
                pig_word = self.translate_word(word)
                # print(pig_word + punctuation)
                self.pig_list.append(pig_word + punctuation)
            # handles lower case words with no punctuation
            else:
                pig_word = self.translate_word(word)
                self.pig_list.append(pig_word)

        pig_string = " ".join(self.pig_list)
        print(pig_string)

    # convert_words()
