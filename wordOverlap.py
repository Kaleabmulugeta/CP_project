file_paths = ['./assets/amharic/cleantext.txt', './assets/tigrigna/cleantext.txt']
def read_file(file):
    with open(file, 'r', encoding='utf-8') as file:
        return file.read()

def word_freq(file):
    words = {}
    data = read_file(file).split()
    for word in data:
        words[word] = words.get(word, 0) + 1

def find_common_words():
    st1 = set(read_file(file_paths[0]).split())
    st2 = set(read_file(file_paths[1]).split())
    return st1 & st2
common_words = find_common_words()
print(common_words)
