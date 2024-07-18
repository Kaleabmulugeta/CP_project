import os
from collections import Counter

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def find_common_words(file_paths):
    word_counts = Counter()
    for file in file_paths:
        text = read_file(file)
        words = text.split()
        word_counts.update(words)
    common_words = [word for word, count in word_counts.items() if count == len(file_paths)]
    return common_words

file_paths = ['./assets/amharic/cleantext.txt', './assets/tigrigna/cleantext.txt']
common_words = find_common_words(file_paths)
print(common_words)
