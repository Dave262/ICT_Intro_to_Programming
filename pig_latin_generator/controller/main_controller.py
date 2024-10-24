class TextConvert:
      def __init__(self):
        super().__init__()
        
        
        self.vowels = "aeiouAEIOU"
        

        
      def get_text(self, textbox):
        
        input_sentence:str = textbox.get('1.0', "end") 
        print(input_sentence)
        self.convert_sentence(input_sentence)
        
      
      
      def convert_to_pig_latin(self, word):
        if word[0] in self.vowels:
          return word+"way"
        
        else:
            # Find where the first vowel is located in the word
            for i, letter in enumerate(word):
                if letter in self.vowels:
                    # Move the consonant cluster to the end and add 'ay'
                    return word[i:] + word[:i] + "ay"
            # If no vowels found, treat it as a single consonant word
            return word + "ay"

          
      def convert_sentence(self, sentence):
        words = sentence.split()
        # Convert each word in the sentence
        pig_latin_words = [self.convert_to_pig_latin(word) for word in words]
        return " ".join(pig_latin_words)
      
      
      
      
if __name__=="__main__":
  controller = TextConvert()
  get_text = controller.get_text("just some text")
  convert_sentece = controller.convert_sentence(get_text)
  print(convert_sentece)
       

            
        
        