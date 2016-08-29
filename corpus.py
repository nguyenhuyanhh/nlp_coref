import os
import re
from multiprocessing import Pool

from pycorenlp import StanfordCoreNLP

import process
import clean

# clean the corpus
def corpus_clean(old_path,new_path):
	for root, dirs, files in os.walk(old_path):
		for f in files:
			# mirror dir structure 
			root_out = root.replace(old_path,new_path,1)
			if (not os.path.isdir(root_out)):
				os.makedirs(root_out)
			file_in_path = os.path.join(root,f)
			file_out_path = os.path.join(root_out,f)
			with open(file_in_path,'r') as f_in, open(file_out_path,'w') as f_out:
				text_in = f_in.read()
				print('read: ' + file_in_path) # debugging
				f_out.write(clean.clean(text_in))
				print('write: ' + file_out_path) # debugging

# normalize the corpus
def corpus_normalize(old_path, new_path, server):
	if (isinstance(server,StanfordCoreNLP)):
		for root, dirs, files in os.walk(old_path):
			for f in files:
				# mirror dir structure 
				root_out = root.replace(old_path,new_path,1)
				if (not os.path.isdir(root_out)):
					os.makedirs(root_out)
				file_in_path = os.path.join(root,f)
				file_out_path = os.path.join(root_out,f)
				with open(file_in_path,'r') as f_in, open(file_out_path,'w') as f_out:
					text_in = f_in.read()
					print('read: ' + file_in_path) # debugging
					text_clean = clean.clean(text_in)
					if (text_clean == ''): # cannot normalize empty text
						f_out.write('')
					else:
						f_out.write(clean.remove_multiple_whitespace(process.normalize(text_clean,server)))
					print('write: ' + file_out_path) # debugging
	else:
		print('CoreNLP error!')
		return None

# the multi-processor
def normalize_m(root, root_out, f, server):
	file_in_path = os.path.join(root,f)
	file_out_path = os.path.join(root_out,f)
	with open(file_in_path,'r') as f_in, open(file_out_path,'w') as f_out:
		text_in = f_in.read()
		print('read: ' + file_in_path) # debugging
		text_clean = clean.clean(text_in)
		if (text_clean == ''): # cannot normalize empty text
			f_out.write('')
		else:
			f_out.write(clean.remove_multiple_whitespace(process.normalize(text_clean,server)))
		print('write: ' + file_out_path) # debugging

# multi-processing the normalization
def corpus_normalize_m(old_path, new_path, server):
	if (not isinstance(server,StanfordCoreNLP)):
		print('CoreNLP error!')
		return None

	file_list = list()
	for root, dirs, files in os.walk(old_path):
		for f in files:
			root_out = root.replace(old_path,new_path,1)
			if (not os.path.isdir(root_out)):
				os.makedirs(root_out)
			file_list.append((root,root_out,f,server))

	pool = Pool(4)
	for file_tuple in file_list:
		pool.apply_async(normalize_m,file_tuple)
	pool.close()
	pool.join()