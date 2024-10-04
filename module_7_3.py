import re  # Модуль re позволяет анализировать текстовые файлы и находить позиции и количество заданных слов.

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                # Читаем файл, приводим к нижнему регистру и убираем пунктуацию
                text = f.read().lower()
                text = re.sub(r"[',.=?;:!+-]", '', text)  # Удаляем пунктуацию
                words = text.split()  # Разбиваем на слова
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()  # Приводим к нижнему регистру
        results = {}
        for name, words in self.get_all_words().items():
            if word in words:
                results[name] = words.index(word) + 1  # Позиция слова
        return results

    def count(self, word):
        word = word.lower()  # Приводим к нижнему регистру
        results = {}
        for name, words in self.get_all_words().items():
            results[name] = words.count(word)  # Количество слова
        return results


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
