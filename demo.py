# demo script
from time import time

import main

text = open('./data/input.txt', 'r').read()

# main program
start_time = time()

# clean some text
# text = main.clean(text)
# print(text)

# clean on non ascii characters for some text
text = main.clean_non_ascii(text)
# print(text)

# annotate some text
# print(main.annotate(text))

# coref some text
# print(main.coref(text))

# normalize some text
print(main.normalize(text))

# clean the corpus
# path_in = '/home/nhanh/TDT2_top20'
# path_out = '/home/nhanh/TDT2_top20_cleaned'
# main.corpus_clean(path_in, path_out)

# normalize the corpus
# path_in = '/home/nhanh/test'
# path_out = '/home/nhanh/test_coref'
# main.corpus_normalize(path_in, path_out)

end_time = time()
print('Run time: ' + str(end_time - start_time) + ' seconds')
