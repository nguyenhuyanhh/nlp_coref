"""optionals.crawler: PDF server operations."""

import logging
import os

import pdf_client
from pdf_client import config
from pdf_client.api import book
from pdf_client.multithread.processor import TextProcessor
from pdf_client.multithread.worker import MultiThreadWorker

# load global config
CUR_DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE = os.path.join(CUR_DIR, 'crawler_config.json')
config.load_from_file(CONFIG_FILE)
ROOT_DIR = os.path.dirname(CUR_DIR)
DATA_DIR = os.path.join(os.path.dirname(ROOT_DIR), 'data/')


def book_list():
    """Get a list of book_id's."""
    return [book_dict['id'] for book_dict in book.List().execute()]


def book_download_raw(book_id):
    """Download all raw sections from a book into individual files."""
    book_dir = os.path.join(DATA_DIR, 'raw_{}'.format(book_id))
    if not os.path.isdir(book_dir):
        os.makedirs(book_dir)

    class SectionDownloader(TextProcessor):
        """Download a Section."""

        def process(self, text, section_id):
            path = os.path.join(book_dir, '{}.txt'.format(section_id))
            with open(path, 'w+') as file_:
                file_.write(text)
            return text

    logging.basicConfig()
    logging.getLogger(
        pdf_client.multithread.worker.__name__).setLevel(logging.INFO)
    worker = MultiThreadWorker(processor=SectionDownloader(), book=book_id)
    worker.start()


def book_download_raw_all():
    """Download all raw sections from all books."""
    for book_id in book_list():
        book_download_raw(book_id)
