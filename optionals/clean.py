"""optionals.clean: Cleaning library."""

import re
import os

KNOWN_REPLACEMENTS = [
    ('``', '"'), ("''", '"'), ('_', '-'), ('–', '-')
]

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(CUR_DIR, 'clean_english_words.txt'), 'r') as file_:
    WORD_LIST = set(word.strip().lower() for word in file_)


def is_english(word_):
    """Helper function to check for English words."""
    return word_.lower().strip('.,!()') in WORD_LIST


def remove_multiple_whitespace(str_):
    """Helper function to remove instances of multiple whitespaces."""
    return re.sub(r'\s+', ' ', str_).strip()


def string_validation(str_):
    """Check for valid lines."""
    lines = list()
    for line in str_.splitlines():
        if line == '\n' or line.startswith(',') or line.startswith('.') or len(line.split()) == 1:
            lines.append('')
        else:
            lines.append(line)
    return '\n'.join(lines)


def join_broken_words(str_):
    """Join broken words, i.e. 'bro- ken'."""
    return re.sub(r'\b- \b', '', str_)


def known_replacements(str_):
    """Do known replacements."""
    for pair in KNOWN_REPLACEMENTS:
        str_ = str_.replace(pair[0], pair[1])
    return str_


def remove_non_ascii(str_):
    """Remove all non-ASCII characters."""
    return re.sub(r'[^\x00-\x7F]', '', str_)


def check_english(str_):
    """Check for English."""
    lines = list()
    for line in str_.strip().splitlines():
        result_line = list()
        for word in line.strip().split():
            if is_english(word):
                result_line.append(word)
            else:
                result_line.append('[FORMULA]')
        lines.append(' '.join(result_line))
    return '\n'.join(lines)


def mult_to_single_line(str_):
    """Join all lines in a text."""
    str_ = remove_multiple_whitespace(str_)
    return ' '.join(str_.split('\n')).strip()


def merge_placeholder(str_):
    """Merge placeholders."""
    lines = list()
    for line in str_.splitlines():
        lines.append(re.sub(r'(\[FORMULA\]([,.] ?)?){2,}', '[FORMULA]', line))
    return '\n'.join(lines)


class Clean():
    """Cleaning operations"""
    default_methods = [
        string_validation,
        join_broken_words,
        known_replacements,
        remove_non_ascii,
        check_english,
        mult_to_single_line,
        merge_placeholder
    ]

    def __init__(self, method_list=default_methods):
        self.methods = method_list

    def clean(self, txt, debug=0):
        """Apply cleaning methods in order."""
        for method in self.methods:
            txt = method(txt)
            if debug:
                print('\n\n{}\n\n{}'.format(method, txt))
        return txt
