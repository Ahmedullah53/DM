import numpy as np
import nltk
from nltk.corpus import treebank
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
nltk.download('treebank')

def seprator(heading):
    print('\n=========================================={}=========================================='.format(heading))

def print_list(lst_of_lst):
    seprator('LIST')
    for lst in lst_of_lst:
        print(lst)

def print_dict(dictionary):
    seprator('DICTIONARY')
    for key, value in dictionary.items():
        print('{} : {}'.format(key, value))

text_corpus = [
    "My name is Ahmed",
    "I have a friend named Ahmed, too",
    "Human machine interface for lab abc computer applications",
    "A survey of user opinion of computer system response time",
    "The EPS user interface management system",
    "System and human system engineering testing of EPS",
    "Relation of user perceived response time to error measurement",
    "The generation of random binary unordered trees",
    "The intersection graph of paths in trees",
    "Graph minors IV Widths of trees and well quasi ordering",
    "Graph minors A survey",
]

''' text_corpus => tokens => tagged => entities'''

stoplist = set()
token_lst = [nltk.word_tokenize(sentence) for sentence in text_corpus]
tagged_lst = [nltk.pos_tag(tokens) for tokens in token_lst]
entities = nltk.chunk.ne_chunk(tagged_lst[2])
# tagged = nltk.pos_tag(['At', 'eight', "o'clock", 'on', 'Thursday', 'morning',
# 'Arthur', 'did', "n't", 'feel', 'very', 'good', '.'])
print_list(token_lst)
print_list(tagged_lst)
print(entities)

t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()