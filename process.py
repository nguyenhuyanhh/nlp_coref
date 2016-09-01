import re
import json

from pycorenlp import StanfordCoreNLP

class Process:
	# start CoreNLP server, use sample text to initialize all annotators
	def __init__(self, uri='http://localhost:9000', props={'annotators':'tokenize,ssplit,pos,ner,lemma,parse,dcoref','outputFormat':'json'}):
		self.SERVER_URI = uri
		self.SERVER = StanfordCoreNLP(self.SERVER_URI)
		self.PROPERTIES = props
		if (self.SERVER.annotate('test',properties=self.PROPERTIES)):
			print('CoreNLP initialized')
		else:
			print('CoreNLP error!')

	# annotate text and return json
	def annotate_txt(self,txt,output_to_file=0):
		json_out = self.SERVER.annotate(txt,properties=self.PROPERTIES)
		
		if (output_to_file == 1):
			with open('output.json','w') as out_file:
				json.dump(json_out,out_file,indent=2)

		return json_out

	# pretty-print out just corefs
	def coref_print(self,txt,significant_corefs=1):
		if (significant_corefs != (0 or 1)):
			return None

		json_out = self.SERVER.annotate(txt,properties=self.PROPERTIES)
		for coref_id in json_out['corefs']:
			if(len(json_out['corefs'][coref_id]) > significant_corefs):
				print('coref chain (id = ' + coref_id + ')')
				for mention_dict in json_out['corefs'][coref_id]:
					print('\t\'' + mention_dict['text'] + '\' in sentence ' + str(mention_dict['sentNum']))

	# normalize a given text (string)
	def normalize(self,txt):
		SPECIAL_TOKEN_LIST = ["'s",',','.',';',':','?','!']
		
		json_out = self.SERVER.annotate(txt,properties=self.PROPERTIES)

		# generate tokens dictionary
		tokens = dict()
		for sentence_dict in json_out['sentences']:
			tok = list()
			for t in sentence_dict['tokens']:
				tok.append(t['originalText'])
			tokens[sentence_dict['index']] = tok
		# print(tokens) # debugging

		# generate replacement table, using only coref chains with >1 mention
		repl_table = dict()
		for coref_id in json_out['corefs']:
			if(len(json_out['corefs'][coref_id])>1):
				mention_pos = list()
				for mention_dict in json_out['corefs'][coref_id]:
					if(mention_dict['isRepresentativeMention']):
						rep_mention = mention_dict['text']
						rep_mention_sent = mention_dict['sentNum']-1
					else:
						mention_pos.append((mention_dict['sentNum']-1,mention_dict['startIndex']-1,mention_dict['endIndex']-2))
				for m in mention_pos:
					if (m[0] != rep_mention_sent): # avoid replacing mentions in the same sentence
						repl_table[m] = rep_mention
		# print(repl_table) # debugging

		# replace tokens with representative mentions
		for repl_key in sorted(repl_table.keys()):
			sNum = repl_key[0]
			stIn = repl_key[1]
			endIn = repl_key[2]
			for sentence in tokens.keys():
				if (sNum == sentence):
					tokens[sentence][stIn] = repl_table[repl_key]
					if (tokens[sentence][endIn] == "'s"): # take into account 's, only replace until before the 's
						for i in range(stIn+1, endIn):
							tokens[sentence][i] = ''
					else:
						for i in range(stIn+1, endIn+1):
							tokens[sentence][i] = ''
		# print(tokens) # debugging

		# recreate text
		txt_out = ''
		for sent in tokens.values():
			for tok in sent:
				if tok in SPECIAL_TOKEN_LIST:
					txt_out += (tok)
				else:
					txt_out += (' ' + (tok))

		return txt_out