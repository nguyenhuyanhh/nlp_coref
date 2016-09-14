import re

KNOWN_REPLACEMENTS = [
    ('``', '"'), ("''", '"'), ('_', '-')
]


def known_replacements(_str):
    for pair in KNOWN_REPLACEMENTS:
        _str = _str.replace(pair[0], pair[1])
    return _str


def remove_multiple_whitespace(_str):
    return re.sub(r'\s+', ' ', _str).strip()


def mult_to_singleline(txt):
    txt = remove_multiple_whitespace(txt)
    return ' '.join(txt.split('\n')).strip()


def Clean(txt):
    methods = [
        known_replacements,
        mult_to_singleline
    ]
    for m in methods:
        txt = m(txt)
    return txt
