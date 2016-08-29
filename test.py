# demo script
import time

import process
import corpus
import clean

start_time = time.clock()

# clean the corpus
path_in = '/home/nhanh/TDT2_top20'
path_out = '/home/nhanh/TDT2_top20_cleaned'
corpus.corpus_clean(path_in,path_out)

# normalize the corpus
# nlp = process.initialize()
# path_in = '/home/nhanh/20096'
# path_out = '/home/nhanh/20096_coref'
# corpus.corpus_normalize(path_in,path_out,nlp)

print(time.clock() - start_time)