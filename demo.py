# demo script
import time

from process import Process
from corpus import Corpus
import clean

p = Process()
c = Corpus(p)

start_time = time.time()

# clean the corpus
# path_in = '/home/nhanh/TDT2_top20'
# path_out = '/home/nhanh/TDT2_top20_cleaned'
# c.corpus_clean(path_in,path_out)

# normalize the corpus
path_in = '/home/nhanh/test'
path_out = '/home/nhanh/test_coref'
c.corpus_normalize_m(path_in,path_out)

end_time = time.time()

print(end_time - start_time)