# put your code here.
def word_count(file):
    with open(file) as poem:
        word_counts = {}

        for line in poem:
            line = line.rstrip()
            line = line.split(' ')
            for word in line:
                word_counts[word] = word_counts.get(word, 0) + 1

    def get_count(dct):
        for word, count in dct.iteritems():
            print word, count

    get_count(word_counts)

word_count('test.txt')
word_count('twain.txt')

