import re
# import string
# import os
# import glob

KNOWN_REPLACEMENTS = [
	('``','"'), ("''",'"'), ('_','-')
]

def known_replacements(_str):
	for pair in KNOWN_REPLACEMENTS:
		_str = _str.replace(pair[0],pair[1])
	return _str


def remove_multiple_whitespace(_str):
	return re.sub(r'\s+', ' ', _str).strip()

def mult_to_singleline(txt):
	txt = remove_multiple_whitespace(txt)
	return ' '.join(txt.split('\n')).strip()

def clean(txt):
	methods = [
		known_replacements,
		mult_to_singleline
	]
	for m in methods:
		txt = m(txt)
	return txt

# def remove_formula(string):
# 	#function count punctuation
# 	count = lambda l1,l2: sum([1 for x in l1 if x in l2])
	
# 	num_comma = string.count(',')
# 	num_fullstop = 0
# 	for c in string.split(' '):
# 		if c.endswith('.'):
# 		# count omly full stop at end of a word (full stop in middle of a word may be a float like 3.2)
# 			num_fullstop += 1
# 	if (num_comma + num_fullstop) > 0:
# 	# only return string with , or .
# 		return string
# 	else:
# 		return ''

# def string_validation(string):
# 	string = unicode(string, errors='ignore')
# 	'''
# 	if string != '\n':
# 		return string
# 	else:
# 		return ''
# 	'''
# 	if string == '\n' or string.startswith(',') or string.startswith('.'):
# 		return ''
# 	else:
# 		return string

# # if a line contains only two-, one, or zero-character sequences, it is most definitely a formula/ whitespace/ non-text
# twocharseq = re.compile(r'[a-z]{3,}',re.I)
# # further formulas, those ending with annotations e.g. (1.3) and starting with =
# annot = re.compile(r'\(\d+(.\d+)+\)\n')
# equals = re.compile(r'=[\w\s+-=<>()|]+\n')
# # figures and tables
# fig = re.compile(r'figure[\w\s+-=<>()]+\n',re.I)
# tab = re.compile(r'table[\w\s+-=<>()]+\n',re.I)
# # chapter headings
# ch = re.compile(r'\d+(.\d+)+[\w\s+-=<>()]+\n',re.I)


# for line in file_in:
# 	if (twocharseq.search(line) and not annot.search(line) and not equals.match(line)):
# 		if (ch.match(line)):
# 			text_out+=('\n'+line)
# 		elif (fig.match(line)):
# 			text_out+='<FIG>\n'
# 		elif (tab.match(line)):
# 			text_out+='<TAB>\n'
# 		else:
# 			text_out+=(line)
# 	line_out = string_validation(remove_formula(line))
# 	if (not fig.match(line_out)):
# 		text_out+=line_out

# file_out = open('output.txt','w')
# file_out.write(text_out)
# file_out.close()