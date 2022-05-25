import fitz 

filtered_words = []
wordcounter = []
worddict = {}
counttotal = 0

paths = [r"sample.pdf"]
text = ""

for p in paths:
    with fitz.open(p) as doc:
        for page in doc:
            text += page.get_text()

words = text.split()

for i in words:
    i = i.lower()
    i = i.replace(".", "")
    i = i.replace(",", "")
    i = i.replace("!", "")
    i = i.replace("?", "")
    i = i.replace("0", "")
    i = i.replace("1", "")
    i = i.replace("2", "")
    i = i.replace("3", "")
    i = i.replace("4", "")
    i = i.replace("5", "")
    i = i.replace("6", "")
    i = i.replace("7", "")
    i = i.replace("8", "")
    i = i.replace("9", "")
    i = i.replace("«", "")
    i = i.replace("»", "")
    i = i.replace("™", "")
    i = i.replace("(", "")
    i = i.replace(")", "")
    if i != "" and len(i) != 1:
        filtered_words.append(i)

for x in filtered_words:
    worddict[x] = filtered_words.count(x)
    counttotal += filtered_words.count(x)

sort = {k: v for k, v in sorted(worddict.items(), key=lambda item: item[1])}

for key in sort:
    counted = worddict[key]
    print("Key", key, 'appears', counted, 'times.')

print("The total amount of words is: ", counttotal)
