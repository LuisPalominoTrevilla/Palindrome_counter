"""
    date: 10/07/2016
    created by: Luis Palomino Trevilla
"""


class TextWords(object):

    # Class constructor
    def __init__(self, file_words):
        """
        :param file_words: a .txt file that contains english words
        This class has 2 attributes:
            - words: a list that contains words read from a text file
            - number_palindromes: the number of palindromes that the text file has. Initially set to 0
        """
        self.words = []
        self.read_words_from_file(file_words)  # reads words from a file and stores them in self.words
        self.number_palindromes = 0

    def read_words_from_file(self, file):
        """
        This method reads words from a text file and stores them inside a list of words
        :param file: a .txt file containing english words
        :return: Nothing
        """
        try:
            f = open(file, 'r')  # Read from a file
            for word in f:
                word = word.strip('\n')
                self.words += word.split(" ")
            f.close()
        except FileNotFoundError:
            print("File Not Found!")

    def delete_words(self):
        """
        Erases every word stored in self.words
        :return: Nothing
        """
        self.words = []

    def get_words(self):
        return self.words

    def is_palindrome(self, word):
        """
        Helper function that checks whether a word is a palindrome
        :param word: any word
        :return: True if word is a palindrome/False otherwise
        """
        reversed_word = word[::-1]
        if word == reversed_word:
            return True
        else:
            return False

    def count_palindromes(self):
        """
        :return: the number of palindromes that the text has
        """
        self.number_palindromes = 0
        for word in self.words:
            if self.is_palindrome(word):
                self.number_palindromes += 1  # We found a palindrome!

        return self.number_palindromes

    def __add__(self, other):
        """
        Allows to add words from another object
        :param other: TextWords object
        :return: Nothing
        """
        self.words += other.words


# TEST CASES
text_one = TextWords('words.txt')  # This file contains one palindrome
print(text_one.count_palindromes())  # prints the number of palindromes in text_one
text_two = TextWords('morewords.txt')  # This file contains 3 palindromes
print(text_two.count_palindromes())  # prints the number of palindromes in text_two
text_one + text_two
print(text_one.count_palindromes())  # Should print 4
