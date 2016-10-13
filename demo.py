# demo script
from time import time

import main

text = open('./data/input.txt', 'r').read()

# main program
start_time = time()

# clean some text
# text = main.clean(text)
# print(text)

# clean all non ascii characters for some text
# text = main.clean_non_ascii(text)
# print(text)

# annotate some text
# print(main.annotate(text))

# coref some text
# print(main.coref(text))

# normalize some text
# print(main.normalize(text))

# clean the corpus
# path_in = './data/TDT2_top20'
# path_out = './data/TDT2_top20_cleaned'
# main.corpus_clean(path_in, path_out)

# normalize the corpus
# path_in = '/home/nhanh/test'
# path_out = '/home/nhanh/test_coref'
# main.corpus_normalize(path_in, path_out)

# SVM evaluation of a corpus to support topic classification
# path = './data/TDT2_top20'
# main.svm(path)

# get all raw books from the server
main.get_raw()

end_time = time()
print('Run time: {} seconds'.format(end_time - start_time))
