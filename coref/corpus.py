"""coref.corpus: Multi-processed corpus operations."""

import logging
import os
from multiprocessing import Pool, cpu_count

from coref.process import Process
from optionals.clean import Clean

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)


class Corpus:
    """
    Corpus operations.
    Syntax: Corpus(process_in_use=Process())
    """

    def __init__(self, process_in_use=Process()):
        self.process = process_in_use

    def corpus_clean(self, old_path, new_path):
        """Clean the corpus."""
        file_list = list()
        for root, _, files in os.walk(old_path):
            for file_ in files:
                root_out = root.replace(old_path, new_path, 1)
                if not os.path.isdir(root_out):
                    os.makedirs(root_out)
                file_list.append((root, root_out, file_))

        pool = Pool(cpu_count())
        for file_tuple in file_list:
            pool.apply_async(clean_m, file_tuple)
        pool.close()
        pool.join()

    def corpus_normalize(self, old_path, new_path):
        """Normalize the corpus."""
        file_list = list()
        for root, _, files in os.walk(old_path):
            for file_ in files:
                root_out = root.replace(old_path, new_path, 1)
                if not os.path.isdir(root_out):
                    os.makedirs(root_out)
                file_list.append((self.process, root, root_out, file_))

        pool = Pool(cpu_count())
        for file_tuple in file_list:
            pool.apply_async(normalize_m, file_tuple)
        pool.close()
        pool.join()


def clean_m(root, root_out, file_):
    """Multi-processor for cleaning."""
    file_in_path = os.path.join(root, file_)
    file_out_path = os.path.join(root_out, file_)
    with open(file_in_path, 'r') as f_in, open(file_out_path, 'w') as f_out:
        text_in = f_in.read()
        LOG.info('read: %s', file_in_path)
        f_out.write(Clean(text_in))
        LOG.info('write: %s', file_out_path)


def normalize_m(process_in_use, root, root_out, file_):
    """Multi-processor for normalization."""
    file_in_path = os.path.join(root, file_)
    file_out_path = os.path.join(root_out, file_)
    with open(file_in_path, 'r') as f_in, open(file_out_path, 'w') as f_out:
        text_in = f_in.read()
        LOG.info('read: %s', file_in_path)
        f_out.write(process_in_use.normalize(text_in))
        LOG.info('write: %s', file_out_path)
