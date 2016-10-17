from time import time

from coref.process import Process
from coref.corpus import Corpus
from coref.clean import Clean, known_replacements, remove_non_ascii
from coref.svm import svm_eval
from server.crawler import book_download_raw_all

# inits
init_start_time = time()
proc = Process()
corp = Corpus(proc)
init_end_time = time()
print('Init time: ' + str(init_end_time - init_start_time) + ' seconds')


def clean(txt, debug=0):
    cleaner = Clean()
    return cleaner.clean(txt, debug)


def clean_non_ascii(txt, debug=0):
    cleaner = Clean([known_replacements, remove_non_ascii])
    return cleaner.clean(txt, debug)


def annotate(txt):
    return proc.annotate_txt(txt)


def coref(txt):
    return proc.coref_print(txt)


def normalize(txt):
    return proc.normalize(txt)


def corpus_clean(path_in, path_out):
    return corp.corpus_clean(path_in, path_out)


def corpus_normalize(path_in, path_out):
    return corp.corpus_normalize(path_in, path_out)


def svm(path):
    svm_eval(path)


def download_all():
    book_download_raw_all()
