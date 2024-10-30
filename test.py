import re

capital_dict = {}
word_dict = {}

# ------------
# Translation
# ------------


def translate_word(word):
    vowels = ["a", "e", "i", "o", "u"]
    if word[0] in vowels:
        return word + "yay"

    for i in range(len(word)):
        if word[i] in vowels:
            return word[i:] + word[:i] + "ay"

    return word + "ay"  # No vowels found


def translate_word_capital(word):
    # Perform the standard translation
    pig_latin = translate_word(word)
    # Capitalize the first letter and make the rest lowercase
    return pig_latin.capitalize()


# ----------------------
# Text handling
# ----------------------
def get_text():
    with open("pig_latin_generator/text_files/demo.txt", "r") as text_file:
        output = text_file.read()

    # Use regex to find words and punctuation separately
    individual_words = re.findall(r"\b\w+\b|[.,!?;]", output)

    for word in individual_words:
        if re.match(r"\w+", word):  # If it's a word (not punctuation)
            clean_word = word
            regular_word = clean_word
            capital_dict[regular_word] = (
                regular_word[0].isupper() if regular_word else False
            )

    for key, value in capital_dict.items():
        if not value:
            word_dict[key] = translate_word(key)
        else:
            formatted_word = key.lower()
            word_dict[key] = translate_word_capital(formatted_word)

    # Rebuild the final output with original punctuation in place
    pig_latin_string = []
    for word in individual_words:
        if word in word_dict:
            pig_latin_string.append(word_dict[word])
        else:
            pig_latin_string.append(word)  # Keep punctuation as is

    # Join without adding spaces before punctuation
    final_text = ""
    for word in pig_latin_string:
        if final_text and word in ".,!?;":
            final_text += word  # Append punctuation directly after the last word
        else:
            final_text += (
                " " + word if final_text else word
            )  # Append with a leading space

    final_text = final_text.strip()  # Clean up any leading space
    print(final_text)
    return final_text


# Call the function
get_text()




    


