class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            a = []
            all_words.update({file_name: a})
            with open(file_name, 'r', encoding='utf-8') as f:
                for line in f:
                    line.replace(',', '').replace('!', '').replace('?', '') \
                        .replace(';', '').replace(':', '').replace(' - ', '') \
                        .replace('.', '').replace('=', '')
                    words = line.lower().split()
                    for word in words:
                        a.append(word)
        return all_words
    def find(self, word):
        found_words = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            if word in words:
                found_words[file_name] = words.index(word) + 1
        return found_words

    def count(self, word):
        word = word.lower()
        word_count = {}
        for file_name, words in self.get_all_words().items():
            word_count[file_name] = words.count(word)
        return word_count

# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего