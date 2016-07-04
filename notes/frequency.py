#! /usr/bin/env python2.7
'Word frequency analysis'

# Building a command line tool.
# Add the sh-bang line at the beginning of the file
# To make this script executable:   chmod +x frequency.py
# You can alias it with:            alias frequency="~/sj/frequency.py"
# Or put it on the path:            ln -s ~/sj/frequency.py /usr/local/bin

from collections import Counter
import re

def word_frequency(text, maxwords=50, foldcase=True, word_pattern=r"[A-Za-z\'\-]+"):
    'Break text in words and return the most common words (50 by default)'
    if foldcase:
        text = text.lower()
    words = re.findall(word_pattern, text)
    return Counter(words).most_common(maxwords)

if __name__ == '__main__':
    from pprint import pprint
    import sys

    if len(sys.argv) != 2:
        print >> sys.stderr, "Usage:  frequency filename"
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename) as f:
        play = f.read()
    pprint(word_frequency(play, maxwords=10))
