from time import time
import os
import random
import re

from coref.process import Process
from coref.clean import Clean

# inits
p = Process()

# test the term model
# data_dirs = ['raw_7', 'raw_8', 'raw_9', 'raw_10', 'raw_11']
# for dir in data_dirs:
#     count_files = 0
#     count_files_occur = 0
#     count_words_occur = 0
#     path = './data/' + dir
#     for root, dirs, files in os.walk(path):
#         for f in files:
#             file = os.path.join(root, f)
#             with open(file, 'r') as fi:
#                 words = re.split('\W+', Clean(fi.read()))
#                 count_words_occur_pre = count_words_occur
#                 if (len(words) > 1):
#                     count_files += 1 
#                 for key in p.TERM_MODEL.keys():
#                     if key in words:
#                         count_words_occur += 1
#                 if (count_words_occur > count_words_occur_pre):
#                     count_files_occur += 1        
#     print('{}: {} sections, {} sections with terms, {} terms'.format(dir, count_files, count_files_occur, count_words_occur))

# test the cleaner
path = './data/raw_9'
for root, dirs, files in os.walk(path):
    f = random.choice(files)
    print('{}\n'.format(f))
    with open(os.path.join(root,f), 'r') as file:
        txt = file.read()
        print(txt)
        Clean(txt, debug=1)
