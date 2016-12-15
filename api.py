"""api: API wrapper for coref.* and optionals.*"""

import logging
from time import time

from coref.process import Process
from coref.corpus import Corpus
from optionals.clean import Clean, known_replacements, remove_non_ascii
from optionals.svm import svm_eval
from optionals.crawler import book_download_raw_all

# inits
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)
INIT_START = time()
PROC = Process()
CORP = Corpus(PROC)
INIT_END = time()
LOG.info('Init time: %s seconds', INIT_END - INIT_START)


def clean(txt, debug=0):
    """optionals.clean.Clean().clean"""
    cleaner = Clean()
    return cleaner.clean(txt, debug)


def clean_non_ascii(txt, debug=0):
    """optionals.clean.Clean([]).clean"""
    cleaner = Clean([known_replacements, remove_non_ascii])
    return cleaner.clean(txt, debug)


def annotate(txt):
    """coref.process.Process().annotate_txt"""
    return PROC.annotate_txt(txt)


def coref(txt):
    """coref.process.Process().coref_print"""
    return PROC.coref_print(txt)


def normalize(txt):
    """coref.process.Process().normalize"""
    return PROC.normalize(txt)


def corpus_clean(path_in, path_out):
    """coref.corpus.Corpus().corpus_clean"""
    return CORP.corpus_clean(path_in, path_out)


def corpus_normalize(path_in, path_out):
    """coref.corpus.Corpus().corpus_normalize"""
    return CORP.corpus_normalize(path_in, path_out)


def svm(path):
    """optionals.svm.svm_eval"""
    svm_eval(path)


def download_all():
    """optionals.crawler.book_download_raw_all"""
    book_download_raw_all()
