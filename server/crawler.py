import logging
import os

import pdf_client
from pdf_client import config
from pdf_client.multithread.processor import TextProcessor
from pdf_client.multithread.worker import MultiThreadWorker

if not os.path.isdir("../data/raw_10"):
    os.makedirs("../data/raw_10")

# download all sections in a book into individual files
class SectionDownloader(TextProcessor):
    def process(self, text, section_id):
        with open("../data/raw_10/{id}.txt".format(id=section_id), 'w+') as file:
            file.write(text)
        return text

def main():
    # enable INFO level logging
    logging.basicConfig()
    logging.getLogger(pdf_client.multithread.worker.__name__).setLevel(logging.INFO)

    # load global config
    config.load_from_file('./config.json')

    # create a worker and start
    worker = MultiThreadWorker(processor=SectionDownloader(), book=10, threads=20)
    worker.start()

if __name__ == '__main__':
    main()