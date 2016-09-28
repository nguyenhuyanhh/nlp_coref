from time import time

from coref.process import Process
from coref.corpus import Corpus
from coref.clean import Clean

# inits
init_start_time = time()
p = Process()
c = Corpus(p)
init_end_time = time()
print('Init time: ' + str(init_end_time - init_start_time) + ' seconds')

# wrappers
def clean(txt):
    return Clean(txt)


def annotate(txt):
    return p.annotate_txt(txt)


def coref(txt):
    return p.coref_print(txt)


def normalize(txt):
    return p.normalize(txt)


def corpus_clean(path_in, path_out):
    return c.corpus_clean(path_in, path_out)


def corpus_normalize(path_in, path_out):
    return c.corpus_normalize(path_in, path_out)