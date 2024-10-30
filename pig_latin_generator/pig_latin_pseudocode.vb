FUNCTION pig_latin (text)
  ' # Split the input text into a list of words

  SET words = SPLIT(text)

  ' initialise an empty list to hold transformed words

  SET pigged_text = [EMPTY LIST]


  FOR each word IN words DO
  ' Transform the word by moving the first letter to the end and adding 'ay'
    SET transformed_word = word[1:] + word[0] + "ay"

    ' Add the transformed word to the pigged_text list
    APPEND transformed_word TO pigged_text

  END FOR

  ' join the transformed words into a single string and return
  RETURN JOIN(pigged_text, " ")
END FUNCTION   

' call the pig_latin function with a sample input and print the result 

PRINT pig_latinf("hello how are you")


