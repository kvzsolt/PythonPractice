import re

def parse_user_data(line):
    """
    >>> parse_user_data('John Doe john.doe@example.com')
    ('John', 'Doe', 'john.doe', 'example.com')
    """
    return (tuple(re.split('@|, |\s',line)))


def compare_lists(dir_a, dir_b):
    """
    dir_a = ['hello.py', 'readme.txt']
    dir_b = ['readme.txt', 'install.txt', 'hello2.py']    
    {'removed': ['hello.py'], 'added': ['hello2.py', 'install.txt']}
    """
    removed = (list(set(dir_a)-set(dir_b)))
    added = (list(set(dir_b)-set(dir_a)))
    return {'removed': sorted(removed), 'added': sorted(added)}


def print_log(message, process_id, timestamp, level=2):
    """
    >>> from datetime import datetime
    >>> print_log('System started!', 1532, datetime(2019, 1, 2, 10, 30, 55).isoformat(' '))
    2019-01-02 10:30:55 [1532] [INFO] System started!
    """
    print('{} [{}] [{}] {}'.format(timestamp,process_id,level,message))

def biggest_rectangle(rectangles):
    """
    Find the biggest rectangle in a sequence.
    Rectangles are represented as tuples of (width, height).

    >>> biggest_rectangle([(2, 4), (3, 3), (4, 2)])
    (3, 3)
    """
    return (max(rectangles, key = lambda x: x[1]*x[0]))



def find_in_file(pattern):
    """
    Find a pattern in file. Print out all lines that match the pattern
    (case-insensitive) with line numbers.

    >>> find_in_file('nevermore', 'raven.txt')
     62 Quoth the Raven, "Nevermore."
     69 With such name as "Nevermore."
     77 Then the bird said, "Nevermore."
     84 Of 'Never- nevermore'."
     92 Meant in croaking "Nevermore."
     99 She shall press, ah, nevermore!
    107 Quoth the Raven, "Nevermore."
    115 Quoth the Raven, "Nevermore."
    123 Quoth the Raven, "Nevermore."
    132 Quoth the Raven, "Nevermore."
    140 Shall be lifted- nevermore!
    """
    
    for index,line in enumerate(open(r'D:\Programming\WEB\2nd_weekpair\python-on-steroids-python-kvzsolt\raven.txt')):
        if pattern in line or pattern.lower() in line and line.strip():
            print(f"{index}{line}".strip())
   
def read_long_words(min_length=5):
    """
    >>> words = read_long_words('raven.txt', 5)
    >>> words[:6]
    ['midnight', 'dreary', 'pondered', 'quaint', 'curious', 'volume']
    """
    
    file = open(r'D:\Programming\WEB\2nd_weekpair\python-on-steroids-python-kvzsolt\raven.txt')
    words = file.read().split()
    return([word for word in words if len(word)>= min_length])
    

def top_words(n=10):
    """
    Find top N words in a file. Return a list of tuples (word, count).

    >>> words = read_long_words('raven.txt', 5)
    >>> top_words(words, 5)
    [('chamber', 11), ('nevermore', 10), ('lenore', 8), ('nothing', 7), ('tapping', 5)]
    """
    file = open(r'D:\Programming\WEB\2nd_weekpair\python-on-steroids-python-kvzsolt\raven.txt')
    words = file.read().split()    
    word_counts = {word: words.count(word) for word in words}
    result = sorted([(value, key) for key, value in word_counts.items()], key = lambda x:x[0], reverse = True)
    return result[:n]