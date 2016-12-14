import logging
import os

import pdf_client
from pdf_client import config
from pdf_client.api import book
from pdf_client.multithread.processor import TextProcessor
from pdf_client.multithread.worker import MultiThreadWorker

# load global config
cur_dir = os.path.dirname(os.path.realpath(__file__))
config_file = os.path.join(cur_dir, 'crawler_config.json')
config.load_from_file(config_file)
data_dir = os.path.join(os.path.dirname(cur_dir), 'data/')


def book_list():
    """get a list of book_id's"""
    book_list = list()
    book_list_api = book.List().execute()
    for book_dict in book_list_api:
        book_list.append(book_dict['id'])
    return book_list


def book_download_raw(book_id):
    """download all raw sections from a book into individual files"""
    # create folder for book
    book_dir = os.path.join(data_dir, 'raw_{}'.format(book_id))
    if not os.path.isdir(book_dir):
        os.makedirs(book_dir)

    class SectionDownloader(TextProcessor):

        def process(self, text, section_id):
            with open(os.path.join(book_dir, '{}.txt'.format(section_id)), 'w+') as file:
                file.write(text)
            return text

    # enable INFO level logging
    logging.basicConfig()
    logging.getLogger(
        pdf_client.multithread.worker.__name__).setLevel(logging.INFO)

    # create a worker and start
    worker = MultiThreadWorker(processor=SectionDownloader(), book=book_id)
    worker.start()


def book_download_raw_all():
    """download all raw sections from all books"""
    for book_id in book_list():
        book_download_raw(book_id)
