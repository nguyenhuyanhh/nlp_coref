import os
from multiprocessing import Pool, cpu_count

from coref.process import Process
from coref.clean import Clean


class Corpus:

    def __init__(self, process_in_use):
        self.PROCESS = process_in_use

    # clean the corpus
    def corpus_clean(self, old_path, new_path):
        file_list = list()
        for root, dirs, files in os.walk(old_path):
            for f in files:
                root_out = root.replace(old_path, new_path, 1)
                if (not os.path.isdir(root_out)):
                    os.makedirs(root_out)
                file_list.append((root, root_out, f))

        pool = Pool(cpu_count())
        for file_tuple in file_list:
            pool.apply_async(clean_m, file_tuple)
        pool.close()
        pool.join()

    # normalize the corpus with multi-processing
    def corpus_normalize(self, old_path, new_path):
        file_list = list()
        for root, dirs, files in os.walk(old_path):
            for f in files:
                root_out = root.replace(old_path, new_path, 1)
                if (not os.path.isdir(root_out)):
                    os.makedirs(root_out)
                file_list.append((self.PROCESS, root, root_out, f))

        pool = Pool(cpu_count())
        for file_tuple in file_list:
            pool.apply_async(normalize_m, file_tuple)
        pool.close()
        pool.join()


# multi-processor for cleaning
def clean_m(root, root_out, f):
    file_in_path = os.path.join(root, f)
    file_out_path = os.path.join(root_out, f)
    with open(file_in_path, 'r') as f_in, open(file_out_path, 'w') as f_out:
        text_in = f_in.read()
        print('read: ' + file_in_path)  # debugging
        f_out.write(Clean(text_in))
        print('write: ' + file_out_path)  # debugging


# multi-processor for normalization
def normalize_m(process_in_use, root, root_out, f):
    file_in_path = os.path.join(root, f)
    file_out_path = os.path.join(root_out, f)
    with open(file_in_path, 'r') as f_in, open(file_out_path, 'w') as f_out:
        text_in = f_in.read()
        print('read: ' + file_in_path)  # debugging
        text_clean = Clean(text_in)
        if (text_clean == ''):  # cannot normalize empty text
            f_out.write('')
        else:
            f_out.write(
                clean.remove_multiple_whitespace(
                    process_in_use.normalize(text_clean)))
        print('write: ' + file_out_path)  # debugging
