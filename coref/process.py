"""coref.process: Coreference resolution process."""

import json
import logging
import os
import re

from pycorenlp import StanfordCoreNLP

# init paths, init and silence loggers
CUR_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(CUR_DIR)
OPTIONALS_DIR = os.path.join(ROOT_DIR, 'optionals/')
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)
logging.getLogger(
    'requests.packages.urllib3.connectionpool').setLevel(logging.ERROR)


class Process:
    """
    Class for coref process.
    Syntax: Process(config_file='process_config.json')
    """

    def __init__(self, config_file='process_config.json'):
        config = json.load(open(os.path.join(CUR_DIR, config_file), 'r'))
        self.server_url = config['url']
        self.server = StanfordCoreNLP(self.server_url)
        self.server_props = config['props']
        if self.server.annotate('a', properties=self.server_props):
            LOG.info('CoreNLP initialized')
        else:
            LOG.info('CoreNLP error!')
        if config['term_model']:
            model = dict()
            model_path = os.path.join(OPTIONALS_DIR, config['term_model'])
            with open(model_path, 'r') as model_file:
                for line in model_file:
                    # only split after first space
                    tmp = line.split(maxsplit=1)
                    model[tmp[0]] = tmp[1].rstrip('\n')
            self.term_model = model

    def replace_terms(self, txt):
        """Use the term model on txt."""
        result = txt
        for abbr, full in self.term_model:
            find = r'\b{word}\b'.format(word=abbr)
            replace = ' {} '.format(full)
            result = re.sub(find, replace, result)
        return result

    def annotate_txt(self, txt):
        """Annotate txt and return json."""
        return self.server.annotate(txt, properties=self.server_props)

    def coref_print(self, txt):
        """Pretty-print out just coreferences from txt to terminal."""
        json_out = self.annotate_txt(txt)
        for coref_id in json_out['corefs']:
            if len(json_out['corefs'][coref_id]) > 1:
                print('coref chain (id = {})'.format(coref_id))
                for mention_dict in json_out['corefs'][coref_id]:
                    print('\t"{}" in sentence {}'.format(
                        mention_dict['text'], str(mention_dict['sentNum'])))

    def normalize(self, txt, replace_terms=False):
        """
        Normalize txt.
        Find all corefs and replace them with referenced entities.
        """
        # replace terms if specified before doing anything
        if replace_terms:
            txt = self.replace_terms(txt)
        json_out = self.annotate_txt(txt)

        # generate tokens dictionary
        tokens = dict()
        for sentence_dict in json_out['sentences']:
            sentence_tokens = [[token['originalText'], token['after']]
                               for token in sentence_dict['tokens']]
            tokens[sentence_dict['index']] = sentence_tokens

        # generate replacement table, using only coref chains with >1 mention
        repl_table = dict()
        for coref_id in json_out['corefs']:
            if len(json_out['corefs'][coref_id]) > 1:
                mention_pos = list()
                for mention_dict in json_out['corefs'][coref_id]:
                    if mention_dict['isRepresentativeMention']:
                        rep_mention = mention_dict['text']
                        rep_mention_sent = mention_dict['sentNum'] - 1
                    else:
                        mention_pos.append((mention_dict['sentNum'] - 1,
                                            mention_dict['startIndex'] - 1,
                                            mention_dict['endIndex'] - 2))
                for ment in mention_pos:
                    if ment[0] != rep_mention_sent:
                        # avoid replacing mentions in the same sentence
                        repl_table[ment] = rep_mention

        # replace tokens with representative mentions
        for repl_key, repl_value in sorted(repl_table.items()):
            sentence_no = repl_key[0]
            start_index = repl_key[1]
            end_index = repl_key[2]
            for sentence_index, sentence in tokens.items():
                if sentence_no == sentence_index:
                    temp = sentence[end_index][1]
                    sentence[start_index][0] = repl_value
                    sentence[start_index][1] = ''
                    if sentence[end_index][0] == "'s":
                        # only replace until before the 's
                        for i in range(start_index + 1, end_index):
                            sentence[i][0] = ''
                            sentence[i][1] = ''
                        sentence[end_index][1] = temp
                    else:
                        for i in range(start_index + 1, end_index + 1):
                            sentence[i][0] = ''
                            sentence[i][1] = ''
                        sentence[end_index][1] = temp

        # recreate text, one sentence per line
        txt_out_lines = list()
        for _, sentence in sorted(tokens.items()):
            txt_out_lines.append(
                ''.join([(token_[0] + token_[1]) for token_ in sentence]))
        txt_out = '\n'.join(txt_out_lines)
        return txt_out
