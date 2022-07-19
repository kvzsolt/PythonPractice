import re
import collections

#This is is not created for the good readability, but to show some onliner Python ninja skills.

#
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
    return {'removed': sorted((list(set(dir_a)-set(dir_b)))), 'added': sorted((list(set(dir_b)-set(dir_a))))}


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
    
    for index,line in enumerate(open(r'D:\Programming\Python-Fullstack\2nd_weekpair\python-on-steroids-python-kvzsolt\raven.txt')):
        if pattern in line or pattern.lower() in line and line.strip():
            print(f"{index} {line.strip()}")


def read_long_words(min_length=11):
    """
    >>> words = read_long_words('raven.txt', 5)  
    """    
    return[re.sub('[".,-]|\'','',word.lower()) for word in re.split('\s',open(r'D:\Programming\Python-Fullstack\2nd_weekpair\python-on-steroids-python-kvzsolt\raven.txt').read()) if len(word)>= min_length]


def top_words(n=5):
    """
    Find top N words in a file. Return a list of tuples (word, count).

    """
    return sorted([(key, value) for key,value in {re.sub('[".,-]|\'|\!|','',key.lower()):value for key,value in collections.Counter(open(r'D:\Programming\Python-Fullstack\2nd_weekpair\python-on-steroids-python-kvzsolt\raven.txt').read().split()).items()}.items()], key = lambda x:x[1], reverse = True)[:n]
    