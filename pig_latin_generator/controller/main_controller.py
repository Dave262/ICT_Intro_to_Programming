import re

class TextConvert:
      def __init__(self):
        super().__init__()
        
        
        self.vowels = "aeiouAEIOU"
        

        
      def get_text(self, textbox):
        
        input_sentence:str = textbox.get('1.0', "end").strip() 
        print(input_sentence)
        return input_sentence
        
      
      
      def convert_to_pig_latin(self, word):
          # Preserve punctuation (e.g., "hello!" becomes "ellohay!")
          match = re.match(r"([a-zA-Z]+)([^a-zA-Z]*)", word)  # Split word from punctuation
          if not match:
              return word  # If no match, return the word as is

          word_body, punctuation = match.groups()

          # Handle words starting with vowels
          if word_body[0] in self.vowels:
              pig_latin_word = word_body + "way"
          else:
              # Find where the first vowel is located in the word
              for i, letter in enumerate(word_body):
                  if letter in self.vowels:
                      # Move the consonant cluster to the end and add 'ay'
                      pig_latin_word = word_body[i:] + word_body[:i] + "ay"
                      break
              else:
                  # If no vowel is found, treat it as a single consonant word
                  pig_latin_word = word_body + "ay"

          # Retain capitalization
          if word_body[0].isupper():
              pig_latin_word = pig_latin_word.capitalize()

          # Return the word with punctuation re-attached
          return pig_latin_word + punctuation

          
      def convert_sentence(self, sentence):
        words = sentence.split()
        # Convert each word in the sentence
        pig_latin_words = [self.convert_to_pig_latin(word) for word in words if word]
        print(f"the sentence has been converted")
        
        return " ".join(pig_latin_words)
        

      
if __name__=="__main__":
  controller = TextConvert()
  get_text = controller.get_text("just some text")
  convert_sentece = controller.convert_sentence(get_text)
  print(convert_sentece)
       

            
        
        