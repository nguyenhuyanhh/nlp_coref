# demo script
import time
import os
import string
import random
import re

# from coref.process import Process
# from coref.corpus import Corpus
from coref.clean import Clean, load_model

# inits
init_start_time = time.time()
# p = Process()
# c = Corpus(p)
init_end_time = time.time()
print('Init time: ' + str(init_end_time - init_start_time) + ' seconds')

# main program
start_time = time.time()

# normalize some text
# text_in = open('data/input.txt','r').read()
# print(Clean(p.normalize(Clean(text_in))))

# clean the corpus
# path_in = '/home/nhanh/TDT2_top20'
# path_out = '/home/nhanh/TDT2_top20_cleaned'
# c.corpus_clean(path_in, path_out)

# normalize the corpus
# path_in = '/home/nhanh/test'
# path_out = '/home/nhanh/test_coref'
# c.corpus_normalize_m(path_in, path_out)

# test the model
# model = load_model('./coref/dsp_terms.txt')
# data_dirs = [7, 8, 9, 10, 11]
# for dir in data_dirs:
#     count_files = 0
#     count_files_occur = 0
#     count_words_occur = 0
#     path = './data/raw_' + str(dir)
#     for root, dirs, files in os.walk(path):
#         for f in files:
#             file = os.path.join(root, f)
#             with open(file, 'r') as fi:
#                 words = re.split('\W+', Clean(fi.read()))
#                 count_words_occur_pre = count_words_occur
#                 if (len(words) > 1):
#                     count_files += 1 
#                 for key in model.keys():
#                     if key in words:
#                         count_words_occur += 1
#                 if (count_words_occur > count_words_occur_pre):
#                     count_files_occur += 1        
#     print('Book {}: {} sections, {} sections with terms, {} terms'.format(dir, count_files, count_files_occur, count_words_occur))

# test the cleaner
path = './data/raw_8'
for root, dirs, files in os.walk(path):
    f = random.choice(files)
    print(f, end='\n\n')
    with open(os.path.join(root,f), 'r') as file:
        txt = file.read()
        print(txt, end='\n\n')
        Clean(txt)

end_time = time.time()
print('Run time: ' + str(end_time - start_time) + ' seconds')
