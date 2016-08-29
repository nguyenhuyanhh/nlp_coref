# demo script
import time

import process
import corpus
import clean

nlp = process.initialize()
path_in = '/home/nhanh/20096'
path_out = '/home/nhanh/20096_coref'

start_time = time.clock()
corpus.corpus_normalize(path_in,path_out,nlp)
print(time.clock()-start_time)