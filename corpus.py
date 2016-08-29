import os
import re

from pycorenlp import StanfordCoreNLP

import process
import clean

# clean the corpus
def corpus_clean(old_path,new_path):
	for root, dirs, files in os.walk(old_path):
		# mirror dir structure 
		root_out = root.replace(old_path,new_path,1)
		os.mkdir(root_out)

		for f in files:
			file_in_path = os.path.join(root,f)
			file_out_path = os.path.join(root_out,f)
			with open(file_in_path,'r') as f_in, open(file_out_path,'w') as f_out:
				text_in = f_in.read()
				print(file_in_path) # debugging
				f_out.write(clean.clean(text_in))
				print(file_out_path) # debugging

# normalize the corpus
def corpus_normalize(old_path, new_path, server):
	if (isinstance(server,StanfordCoreNLP)):
		for root, dirs, files in os.walk(old_path):
			for f in files:
				# mirror dir structure 
				root_out = root.replace(old_path,new_path,1)
				if (not os.path.isdir(root_out)):
					os.mkdir(root_out)
				file_in_path = os.path.join(root,f)
				file_out_path = os.path.join(root_out,f)
				with open(file_in_path,'r') as f_in, open(file_out_path,'w') as f_out:
					text_in = f_in.read()
					print(file_in_path) # debugging
					text_clean = clean.clean(text_in)
					if (text_clean == ''): # cannot normalize empty text
						f_out.write('')
					else:
						f_out.write(clean.remove_multiple_whitespace(process.normalize(text_clean,server)))
					print(file_out_path) # debugging
	else:
		print('CoreNLP error!')
		return None