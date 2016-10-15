# demo script
from time import time

import api

text = open('./data/input.txt', 'r').read()

# main program
start_time = time()

# clean some text
# text = api.clean(text)
# print(text)

# clean all non ascii characters for some text
# text = api.clean_non_ascii(text)
# print(text)

# annotate some text
# print(api.annotate(text))

# coref some text
# print(api.coref(text))

# normalize some text
# print(api.normalize(text))

# clean the corpus
# path_in = './data/TDT2_top20'
# path_out = './data/TDT2_top20_cleaned'
# api.corpus_clean(path_in, path_out)

# normalize the corpus
# path_in = '/home/nhanh/test'
# path_out = '/home/nhanh/test_coref'
# api.corpus_normalize(path_in, path_out)

# SVM evaluation of a corpus to support topic classification
# path = './data/TDT2_top20'
# api.svm(path)

# get all raw books from the server
api.get_raw()

end_time = time()
print('Run time: {} seconds'.format(end_time - start_time))
