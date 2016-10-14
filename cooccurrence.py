
import sys

def parse_file( filename ):
    f = open(filename)
    raw = f.read()
    raw_words = raw.split()
    return [ word.lower().strip(".?!',;:0") for word in raw_words]
    

def build_neighbors_frequencies( words, k ):
    neighbors = {}
    counts = {}

    for word_index, word in enumerate( words ):
        iterate_neighbors_set = set()
        if word not in neighbors:
            neighbors[word] = {}

        if word in counts:
                counts[word] += 1
        else:
            counts[word] = 1

        for i in xrange( word_index  - k, word_index + k + 1):
            if i in xrange(len(words)):
                if words[i] not in iterate_neighbors_set and i != word_index:
                    if words[i] in neighbors[word]:
                        neighbors[word][words[i]] += 1
                    else:
                        neighbors[word][words[i]] = 1
                    iterate_neighbors_set.add( words[i] )

    return neighbors, counts


def cooccurrence( anchor_word, compare_word, neighbors, counts ):
    if anchor_word not in neighbors:
        return 0

    return neighbors[anchor_word][compare_word] / float( counts[anchor_word] )



if __name__ == '__main__':
    words = parse_file( sys.argv[1] )
    neighbors, counts = build_neighbors_frequencies( words, int( sys.argv[2] ) )

    while True:
        my_input = raw_input("Enter your input or 'q' to quit: ").split()
        if my_input[0] == 'q':
            break

        print  "%.2f" % cooccurrence( my_input[0], my_input[1], neighbors, counts )
