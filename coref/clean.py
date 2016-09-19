import re

KNOWN_REPLACEMENTS = [
    ('``', '"'), ("''", '"'), ('_', '-'), ('ﬁ', 'fi'), ('ﬀ', 'ff'), 
    ('ﬂ', 'fl'), ('ﬃ', 'ffi'), ('ﬄ', 'ffl')
]

# helper functions
def load_model(file):
    model = dict()
    with open(file, 'r') as model_file:
        for line in model_file:
            tmp = line.split(maxsplit=1)
            model[tmp[0]] = tmp[1].rstrip('\n')
    return model


# rules
def known_replacements(_str):
    for pair in KNOWN_REPLACEMENTS:
        _str = _str.replace(pair[0], pair[1])
    return _str


def remove_non_ascii(_str):
    return re.sub(r'[^\x00-\x7F]', '', text)


def remove_multiple_whitespace(_str):
    return re.sub(r'\s+', ' ', _str).strip()


def mult_to_singleline(txt):
    txt = remove_multiple_whitespace(txt)
    return ' '.join(txt.split('\n')).strip()


# main function
def Clean(txt):
    methods = [
        known_replacements,
        remove_non_ascii,
        mult_to_singleline
    ]
    for m in methods:
        txt = m(txt)
    return txt
