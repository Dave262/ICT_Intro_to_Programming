import re
import string


class TextConvert:
    def __init__(self, txt_file):
        # def run(self):

        self.txt_file = txt_file
        self.capital_dict = {}
        self.pig_list = []
        self.pig_string = ""

        self.convert_words()

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

        # Split the text into lines and maintain line breaks
        lines = output.splitlines()

        # Process each line and capture words along with punctuation
        list_of_words_and_punct = []
        for line in lines:
            regex_pattern = r"(\b[\w'-]+)([.,!?;]?)"
            individual_words = re.findall(regex_pattern, line)
            # Construct final result by appending word and punctuation
            words_with_punct = [
                word + punctuation for word, punctuation in individual_words
            ]
            # Append line breaks to the end of the processed words
            list_of_words_and_punct.extend(
                words_with_punct + ["\n"]
            )  # Add newline after each line

        return list_of_words_and_punct

    def convert_words(self):
        list_of_words = self.get_text()

        for word in list_of_words:
            # Check for line breaks and handle accordingly
            if word == "\n":
                self.pig_list.append("\n")  # Append newline directly to preserve it
                continue

            # Your existing word conversion logic...
            if word[0].isupper() and word.endswith(tuple(string.punctuation)):
                punctuation = word[-1]
                word = word[:-1]
                word = word.lower()
                pig_word = self.translate_word(word)
                pig_word = pig_word[0].upper() + pig_word[1:]
                self.pig_list.append(pig_word + punctuation)
            elif word[0].isupper():
                word = word.lower()
                pig_word = self.translate_word(word)
                pig_word = pig_word[0].upper() + pig_word[1:]
                self.pig_list.append(pig_word)
            elif word.endswith(tuple(string.punctuation)):
                punctuation = word[-1]
                word = word[:-1]
                word = word.lower()
                pig_word = self.translate_word(word)
                self.pig_list.append(pig_word + punctuation)
            else:
                pig_word = self.translate_word(word)
                self.pig_list.append(pig_word)

        # Join the list with spaces, but ensure newlines are maintained
        self.pig_string = " ".join(self.pig_list)  # Maintain spaces between words

        return self.pig_string

    def print(self):
        print(self.pig_string)


if __name__ == "__main__":
    print("Controller is main...")
    print("-------------------------")
    converter = TextConvert("text_files/demo.txt")
    converter.print()
