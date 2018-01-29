import sys
import re
from collections import Counter
TOKENIZE_PATTERN = r"\w+(?:[-'\.]\w+)*"


class Wordcount:

    def __init__(self, filename=None, tokenize_pattern=TOKENIZE_PATTERN):
        # Set variables
        self.word_cound = {}
        self.tokenize_pattern = tokenize_pattern
        self.filename = filename

    def read_file(self):
        """Read file to string"""

        if self.filename is None:
            raise Exception("No filename given")

        with open(self.filename) as f:
            word_data = f.read()

        return word_data

    def update_word_count(self, word_data):
        """Update word counts based on word data string, case insensitive"""

        # transform to lowercase
        word_data = word_data.lower()

        # Count all words given tokenize pattern
        self.word_cound = Counter(re.findall(self.tokenize_pattern, word_data))

    def print_word_counts(self):
        """Print words from word count"""
        for word in self.word_cound:
            count = self.word_cound[word]
            print('{0} {1}'.format(word, count))


def main():
    """Main function takes a file name as argument"""
    # Check that 1 argument for filename was given
    if len(sys.argv) < 2:
        raise Exception('Missing argument: filename')
    elif len(sys.argv) > 2:
        raise Exception('To many arguments, only one filename should be given')

    # create new word count object
    word_count = Wordcount(filename=sys.argv[1])
    # Read word data from file
    word_data = word_count.read_file()
    # Count words in string
    word_count.update_word_count(word_data)
    # Print word count
    word_count.print_word_counts()


if __name__ == '__main__':
    main()
