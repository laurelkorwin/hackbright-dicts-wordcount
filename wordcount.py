# put your code here.
from string import punctuation

def word_count(file):
    with open(file) as poem:
        word_counts = {}

        for line in poem:
            line = line.rstrip()
            line = line.split(' ')
            for word in line:
                word = ''.join(l for l in word if l not in punctuation).lower()
                word_counts[word] = word_counts.get(word, 0) + 1

    def get_count(dct):
        for word, count in dct.iteritems():
            print word, count

    get_count(word_counts)

word_count('test.txt')

