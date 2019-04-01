from nltk.corpus import wordnet as wn
from itertools import chain

lemmas_in_wordnet = set(chain(*[ss.lemma_names() for ss in wn.all_synsets()]))

lemmas_in_wordnet = { lemma for lemma in lemmas_in_wordnet if "_" not in lemma }

lemmas_in_wordnet = { lemma for lemma in lemmas_in_wordnet
                      if lemma.capitalize() != lemma }

lemmas_in_wordnet = { lemma for lemma in lemmas_in_wordnet
                      if lemma.upper() != lemma }

with open('word_dict.txt', 'w') as f:
    for item in lemmas_in_wordnet:
        f.write(f"{item}\n")
