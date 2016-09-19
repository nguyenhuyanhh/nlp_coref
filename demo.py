# demo script
import time
import os

# from coref.process import Process
# from coref.corpus import Corpus
from coref.clean import Clean, load_model

init_start_time = time.time()

# inits
# p = Process()
# c = Corpus(p)

init_end_time = time.time()
print('Init time: ' + str(init_end_time - init_start_time) + ' seconds')

start_time = time.time()

# normalize some text
# text_in = open('data/input.txt','r').read()
# print(Clean(p.normalize(Clean(text_in))))

# clean the corpus
# path_in = '/home/nhanh/TDT2_top20'
# path_out = '/home/nhanh/TDT2_top20_cleaned'
# c.corpus_clean(path_in, path_out)

# normalize the corpus
# path_in = '/home/nhanh/test'
# path_out = '/home/nhanh/test_coref'
# c.corpus_normalize_m(path_in, path_out)

# test the model
model = load_model('./coref/dsp_terms.txt')
data_dirs = [7, 8, 9, 10, 11]
for dir in data_dirs:
    count_files = 0
    count_occur = 0
    path = './data/raw_' + str(dir)
    for root, dirs, files in os.walk(path):
        for f in files:
            file = os.path.join(root, f)
            with open(file, 'r') as fi:
                text = fi.read()
                if (not text == ''):
                	count_files += 1 
                for key in model.keys():
                    if key in text:
                        count_occur += 1
                        break
    print('{}: {} {}'.format(dir, count_files, count_occur)) 

end_time = time.time()
print('Run time: ' + str(end_time - start_time) + ' seconds')
