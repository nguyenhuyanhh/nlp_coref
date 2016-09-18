# demo script
import time

from coref.process import Process
# from coref.corpus import Corpus
from coref.clean import Clean

init_start_time = time.time()

# inits
p = Process()
# c = Corpus(p)

init_end_time = time.time()
print('Init time: ' + str(init_end_time - init_start_time) + ' seconds')

start_time = time.time()

# normalize some text
text_in = open('data/input.txt','r').read()
print(Clean(p.normalize(Clean(text_in))))

# clean the corpus
# path_in = '/home/nhanh/TDT2_top20'
# path_out = '/home/nhanh/TDT2_top20_cleaned'
# c.corpus_clean(path_in, path_out)

# normalize the corpus
# path_in = '/home/nhanh/test'
# path_out = '/home/nhanh/test_coref'
# c.corpus_normalize_m(path_in, path_out)

end_time = time.time()
print('Run time: ' + str(end_time - start_time) + ' seconds')
