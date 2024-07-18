import re

with open("./cp_project/assets/amharic/rawinput.txt","r",encoding="utf8") as fhand:
    raw_text = fhand.read()
    text = re.sub("[\u135D-\u137C]+" , "" , raw_text, flags=re.UNICODE)
    text = re.sub("[0-9A-Za-z]+", "", text)
    clean_text = re.sub("[\\[!@#%\\*\\$()\\^&\\]{}`]+", " ", text)
    with open("./cp_project/assets/amharic/cleantext.txt", "a", encoding="utf8") as f:
        f.write(clean_text)
with open("./cp_project/assets/tigrigna/rawinput.txt","r",encoding="utf8") as fhand:
    raw_text = fhand.read()
    text = re.sub("[\u135D-\u137C]+" , "" , raw_text, flags=re.UNICODE)
    text = re.sub("[0-9A-Za-z]+", "", text)
    clean_text = re.sub("[\\[!@#%\\*\\$()\\^&\\]{}`]+", " ", text)
    with open("./cp_project/assets/tigrigna/cleantext.txt", "a", encoding="utf8") as f:
        f.write(clean_text)