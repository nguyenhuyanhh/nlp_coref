# demo script
import time

import process
import corpus
import clean

nlp = process.initialize()

start_time = time.time()

# clean the corpus
# path_in = '/home/nhanh/TDT2_top20'
# path_out = '/home/nhanh/TDT2_top20_cleaned'
# corpus.corpus_clean(path_in,path_out)

# normalize the corpus
path_in = '/home/nhanh/test'
path_out = '/home/nhanh/test_coref'
corpus.corpus_normalize_m(path_in,path_out,nlp)

end_time = time.time()

print(end_time - start_time)