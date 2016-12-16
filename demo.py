"""demo: Demo script."""

import logging
import os
from time import time

import api

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(CUR_DIR, 'data/')
RESULTS_DIR = os.path.join(CUR_DIR, 'results/')
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)
FILE_ID = 'input_sample_1'
TEXT = open(os.path.join(DATA_DIR, '{}.txt'.format(FILE_ID)), 'r').read()

START = time()

# clean some text
# text = api.clean(text)
# print(text)

# clean all non ascii characters for some text
# text = api.clean_non_ascii(text)
# print(text)

# process some text
api.process(TEXT)

# clean the corpus
# path_in = os.path.join(data_dir, 'TDT2_top20/')
# path_out = os.path.join(data_dir, 'TDT2_top20_cleaned/')
# api.corpus_clean(path_in, path_out)

# normalize the corpus
# path_in = os.path.join(data_dir, 'test/')
# path_out = os.path.join(data_dir, 'test_coref/')
# api.corpus_normalize(path_in, path_out)

# SVM evaluation of a corpus to support topic classification
# path = os.path.join(data_dir, 'TDT2_top20/')
# api.svm(path)

# get all raw books from the server
# api.download_all()

END = time()
LOG.info('Run time: %s seconds', END - START)
