import numpy as np 
from collections import defaultdict
from gensim import corpora, models

def seprator(heading):
    print('=========================================={}=========================================='.format(heading))

text_corpus = [
    "My name is Ahmed",
    "I have a friend named Ahmed too",
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

stoplist = set('for a is in of the and to'.split(' '))
texts = [[word for word in doc.lower().split(' ') if word not in stoplist] for doc in text_corpus]

frequencies = defaultdict(int)
for text in texts:
    for token in text:
        frequencies[token] += 1

ppc = [[token for token in text if frequencies[token] > 1] for text in texts]

for item in ppc:
    print(item)

dictionary = corpora.Dictionary(ppc)
for key, value in dictionary.items():
    print('{} : {}'.format(key, value))

seprator('new vec')
new_doc = 'my name is Ahmed'
new_vec = dictionary.doc2bow(new_doc.lower().split(' '))
print(new_vec)

seprator('heading')
bow_corpus = [dictionary.doc2bow(text) for text in ppc]
print(bow_corpus)

tfid = models.TfidfModel(bow_corpus)
new_words = set('hi i sit in front to Jupiter and i use computers'.lower().split(' '))
print(tfid[dictionary.doc2bow(new_words)])
