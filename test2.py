def dowork(sentence):
    def pigword(word):
        return "".join([word[1:], word[0], "ay"])

    return " ".join([pigword(word) for word in sentence.split()])


dataexp = [
    ("hello how are you", "ellohay owhay reaay ouyay"),
    ("programming in python is fun", "rogrammingpay niay ythonpay siay unfay"),
]

for inp, exp in dataexp:
    got = dowork(inp)
    msg = "exp :%s:  for %s \n      got :%s:" % (exp, inp, got)
    if exp == got:
        print("good! %s" % msg)
    else:
        print("bad ! %s" % msg)

  

