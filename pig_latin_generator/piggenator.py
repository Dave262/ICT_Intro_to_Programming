def pig_latin(text_file):

  user_sentence: str = (input("please say something"))
  converted_text: list = []

  words = user_sentence.split(" ")

  for word in words:
    word = word[1:] + word[0] + "ay"
    converted_text.append(word)
  
  