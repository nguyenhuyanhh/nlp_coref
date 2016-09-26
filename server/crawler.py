import logging
import os

import pdf_client
from pdf_client import config
from pdf_client.multithread.processor import TextProcessor
from pdf_client.multithread.worker import MultiThreadWorker

# set book id
book_id = 11
book_dir = '../data/raw_{}'.format(book_id)
if not os.path.isdir(book_dir):
    os.makedirs(book_dir)

# download all sections from the book into individual files
class SectionDownloader(TextProcessor):
    def process(self, text, section_id):
        with open(os.path.join(book_dir, '{}.txt'.format(section_id)), 'w+') as file:
            file.write(text)
        return text

def main():
    # enable INFO level logging
    logging.basicConfig()
    logging.getLogger(pdf_client.multithread.worker.__name__).setLevel(logging.INFO)

    # load global config
    config.load_from_file('./config.json')

    # create a worker and start
    worker = MultiThreadWorker(processor=SectionDownloader(), book=book_id)
    worker.start()

if __name__ == '__main__':
    main()