from time import time
import os
import random
import re

# test the model
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
#                 for key in p.TERM_MODEL.keys():
#                     if key in words:
#                         count_words_occur += 1
#                 if (count_words_occur > count_words_occur_pre):
#                     count_files_occur += 1        
#     print('Book {}: {} sections, {} sections with terms, {} terms'.format(dir, count_files, count_files_occur, count_words_occur))

# test the cleaner and term model
# path = './data/raw_9'
# for root, dirs, files in os.walk(path):
#     f = random.choice(files)
#     with open('demo.log', 'w') as log:
#         log.write('{}\n'.format(f))
#         with open(os.path.join(root,f), 'r') as file:
#             txt = file.read()
#             clean_txt = Clean(txt)
#             norm_txt = p.replace_terms(clean_txt)
#             log.write('<raw text>\n\n{}\n\n<clean text>\n\n{}\n\n<normalized text>\n\n{}'.format(txt, clean_txt, norm_txt))

            # normalize some text
            # text_in = open('data/input.txt','r').read()
            # log.write('<normalized text>\n\n{}'.format(p.normalize(Clean(txt))))