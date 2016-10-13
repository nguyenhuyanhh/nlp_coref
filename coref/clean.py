import re
import os

KNOWN_REPLACEMENTS = [
    ('``', '"'), ("''", '"'), ('_', '-'), ('–', '-')
]

# helper functions
cur_dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(cur_dir, 'english_words.txt'), 'r') as word_list_file:
    word_list = set(word.strip().lower() for word in word_list_file)

def is_english(_word):
    return _word.lower().strip('.,!()') in word_list


def remove_multiple_whitespace(_str):
    return re.sub(r'\s+', ' ', _str).strip()


# rules
def string_validation(_str):
    lines = list()
    for line in _str.splitlines():
        if line == '\n' or line.startswith(',') or line.startswith('.') or len(line.split()) == 1:
            lines.append('')
        else:
            lines.append(line)
    return '\n'.join(lines)


def join_broken_words(_str):
    return re.sub(r'\b- \b', '', _str)


def known_replacements(_str):
    for pair in KNOWN_REPLACEMENTS:
        _str = _str.replace(pair[0], pair[1])
    return _str


def remove_non_ascii(_str):
    return re.sub(r'[^\x00-\x7F]', '', _str)


def check_english(_str):
    lines = list()
    for line in _str.strip().splitlines():
        result_line = list()
        for word in line.strip().split():
            if is_english(word):
                result_line.append(word)
            else:
                result_line.append('[FORMULA]')
        lines.append(' '.join(result_line))
    return '\n'.join(lines)


def mult_to_single_line(_str):
    _str = remove_multiple_whitespace(_str)
    return ' '.join(_str.split('\n')).strip()

def merge_placeholder(_str):
    lines = list()
    for line in _str.splitlines():
        lines.append(re.sub(r'(\[FORMULA\]([,.] ?)?){2,}', '[FORMULA]', line))
    return '\n'.join(lines)


# main function
class Clean():
    methods = [
        string_validation,
        join_broken_words,
        known_replacements,
        remove_non_ascii,
        check_english,
        mult_to_single_line,
        merge_placeholder
    ]

    def __init__(self, method_list=[]):
        if (len(method_list) > 0):
            self.methods = method_list

    def clean(self, txt, debug=0):
        for m in self.methods:
            txt = m(txt)
            if debug:
                print('\n\n{}\n\n{}'.format(m, txt))
        return txt
