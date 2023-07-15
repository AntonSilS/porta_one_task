from collections import Counter
import regex as re


class Cleanable:
    def clean_punctuation(self, word):
        pattern_punctuation = r'(^["(<])|(\p{P}$)'
        filtered_word = re.sub(pattern_punctuation, '', word)
        return filtered_word

    def check_start_symbol(self, user_string: str) -> bool:
        pattern_start_letter = r'[a-zA-Zа-яА-ЯҐєЄіІїЇ"(<]'
        match = re.match(pattern_start_letter, user_string.strip())
        if match:
            return True
        else:
            return False

    def clean_words(self, words: list) -> list:
        filtered_words = []
        for word in words:
            filtered_word = self.clean_punctuation(word)
            result = self.check_start_symbol(filtered_word)
            if filtered_word and result:
                filtered_words.append(filtered_word)
        return filtered_words


class DividerText:
    def divide_text(self, text):
        return text.split()


class Searcher:
    def find_unique_symbol(self, sequence: list|str) -> str:
        result = Counter(sequence)
        for symbol in sequence:
            if result[symbol] == 1:
                return symbol

    def get_unique_symbols(self, words_lst: list) -> list[str]:
        unique_symbols = []
        for word in words_lst:
            letter = self.find_unique_symbol(word)
            if letter:
                unique_symbols.append(letter)
        return unique_symbols


class AnalyzerText(Cleanable):
    def __init__(self, text, divider: DividerText, searcher: Searcher):
        self.text = text
        self.divider = divider
        self.searcher = searcher

    def analyze_unique(self) -> list[str]:
        if self.check_start_symbol(self.text):
            split_text = self.divider.divide_text(self.text)
            clear_words = self.clean_words(split_text)
            return self.searcher.get_unique_symbols(clear_words)
        else:
            return ["it is not a text!!!"]

    def get_most_unique_symbol(self) -> str:
        unique_symbols_lst = self.analyze_unique()
        print(unique_symbols_lst)

        most_unique_symbol = self.searcher.find_unique_symbol(unique_symbols_lst)
        print(most_unique_symbol)
        return most_unique_symbol





