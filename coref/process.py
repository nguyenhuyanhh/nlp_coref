import json
import os
import re

from pycorenlp import StanfordCoreNLP


class Process:
    # class variables
    SERVER = None
    SERVER_URL = None
    SERVER_PROPS = None
    TERM_MODEL = None

    # start CoreNLP server, use sample text to initialize all annotators, load term model
    def __init__(self, config_file='config.json'):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        config = json.load(open(os.path.join(cur_dir, config_file), 'r'))
        self.SERVER_URL = config['url']
        self.SERVER = StanfordCoreNLP(self.SERVER_URL)
        self.SERVER_PROPS = config['props']
        if (self.SERVER.annotate('a', properties=self.SERVER_PROPS)):
            print('CoreNLP initialized')
        else:
            print('CoreNLP error!')
        model = dict()
        with open(os.path.join(cur_dir, config['term_model']), 'r') as model_file:
            for line in model_file:
                tmp = line.split(maxsplit=1) # only split after first space
                model[tmp[0]] = tmp[1].rstrip('\n')
        self.TERM_MODEL = model

    # use the term model
    def replace_terms(self, txt):
        result = txt
        for term in self.TERM_MODEL.keys():
            find = r'\b{word}\b'.format(word=term)
            replace = ' {} '.format(self.TERM_MODEL[term])
            result = re.sub(find, replace, result)
        return result

    # annotate text and return json
    def annotate_txt(self, txt):
        return self.SERVER.annotate(txt, properties=self.SERVER_PROPS)

    # pretty-print out just corefs
    def coref_print(self, txt):
        json_out = self.annotate_txt(txt)
        for coref_id in json_out['corefs']:
            if(len(json_out['corefs'][coref_id]) > 1):
                print('coref chain (id = ' + coref_id + ')')
                for mention_dict in json_out['corefs'][coref_id]:
                    print('\t\'' + mention_dict['text'] + '\' in sentence ' +
                          str(mention_dict['sentNum']))

    # normalize a given text (string)
    def normalize(self, txt):
        # replace terms before doing anything
        txt = self.replace_terms(txt)
        json_out = self.annotate_txt(txt)

        # generate tokens dictionary
        tokens = dict()
        for sentence_dict in json_out['sentences']:
            sentence_tokens = list()
            for t in sentence_dict['tokens']:
                sentence_tokens.append(t['originalText'])
            tokens[sentence_dict['index']] = sentence_tokens
        # print(tokens) # debugging

        # generate replacement table, using only coref chains with >1 mention
        repl_table = dict()
        for coref_id in json_out['corefs']:
            if(len(json_out['corefs'][coref_id]) > 1):
                mention_pos = list()
                for mention_dict in json_out['corefs'][coref_id]:
                    if(mention_dict['isRepresentativeMention']):
                        rep_mention = mention_dict['text']
                        rep_mention_sent = mention_dict['sentNum']-1
                    else:
                        mention_pos.append((mention_dict['sentNum']-1,
                                            mention_dict['startIndex']-1,
                                            mention_dict['endIndex']-2))
                for m in mention_pos:
                    if (m[0] != rep_mention_sent):
                        # avoid replacing mentions in the same sentence
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
                    if (tokens[sentence][endIn] == "'s"):
                        # only replace until before the 's
                        for i in range(stIn+1, endIn):
                            tokens[sentence][i] = ''
                    else:
                        for i in range(stIn+1, endIn+1):
                            tokens[sentence][i] = ''
        # print(tokens) # debugging

        # recreate text, one sentence per line
        # use two special tokens list ("no space following" and "no space preceding") 
        SPECIAL_TOKEN_POST = ['(', '[']
        SPECIAL_TOKEN_PRE = ["'s", ',', '.', ';', ':', '?', '!', 'FORMULA', 'FIGURE', ']', ')']
        txt_out_lines = list()
        for sent in tokens.values():
            txt_out_lines.append(' '.join([t for t in sent if t]).strip())
        txt_out = '\n'.join(txt_out_lines)
        for s_token in SPECIAL_TOKEN_POST:
            find = '{} '.format(s_token)
            txt_out = txt_out.replace(find, s_token)
        for s_token in SPECIAL_TOKEN_PRE:
            find = ' {}'.format(s_token)
            txt_out = txt_out.replace(find, s_token)
        return txt_out
