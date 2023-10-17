def count_words(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        contents = file.read()
        words = contents.split()
        freq = {}
        for word in words:
            word = word.strip('.,;!?()-"\'').lower()
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        for word in freq:
            print('{}: {}'.format(word, freq[word]))
count_words('F:\\codeonbytes\\s.txt')
