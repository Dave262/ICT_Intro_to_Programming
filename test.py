
vowels = ["a", "e", "i", "o", "u"]


def get_text():
    latin_words = []
    with open("pig_latin_generator/text_files/demo.txt", "r") as text_file: 
    
        output = text_file.read().lower()
    
    individual_words = output.split(" ")
    
    for word in individual_words:
        has_vowel = False
        for i in range(len(word)):
            if word[0] in vowels:
                latin_words.append(word+"yay")
                break
            else:
                if word[i] in vowels:
                    latin_words.append(word[i:] + word[:i] + "ay")
                    has_vowel = True
                    break
                
                if not has_vowel and (i ==len(word)-1):
                    latin_words.append(word+"ay")
                    break
                  
    pig_latin_text = " ".join(latin_words)
    print(pig_latin_text)




        
        
get_text()



    

    