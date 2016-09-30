import re

KNOWN_REPLACEMENTS = [
    ('``', '"'), ("''", '"'), ('_', '-'), ('–', '-')
]

# regex patterns
formula_pattern = r'\b([ωδ\w]+ ?\([\w ωδ]+\)|[^\s]* =( ?[+−]?\w+([\.,]\d+)? ?)([+−×*]( ?\w+(\.\d+)? ?))*( ?= ?[+−]?\d+(\.\d+)?)?\b|zzz)'
expression_pattern = r'\b( ?[+−]?\w+([\.,]\d+)? ?)([+−×*/]( ?\w+(\.\d+)? ?))+( ?= ?[+−]?\d+(\.\d+)?)?\b'
range_pattern = r'−?(\d+|\w|∞)? [≤≥><] −?(\d+|\w|∞)'

# helper functions
def count_endingfullstop(_str):
    num_fullstop = 0
    for word in _str.strip().split():
        if word.endswith('.'):
            num_fullstop += 1
    return num_fullstop


def is_formula(_str):
    if re.search(r'[A-Za-z]{2,}', _str):
        return False
    else:
        return True


def remove_multiple_whitespace(_str):
    return re.sub(r'\s+', ' ', _str).strip()


# rules
def known_replacements(_str):
    for pair in KNOWN_REPLACEMENTS:
        _str = _str.replace(pair[0], pair[1])
    return _str


def remove_non_ascii(_str):
    return re.sub(r'[^\x00-\x7F]', '', _str)


def string_validation(_str):
    lines = list()
    for line in _str.splitlines():
        if line == '\n' or line.startswith(',') or line.startswith('.') or len(line.split()) == 1:
            lines.append('')
        else:
            lines.append(line)
    return '\n'.join(lines)


def remove_formula(_str):
    lines = list()
    for line in _str.splitlines():
        count = lambda l1, l2: sum([1 for x in l1 if x in l2])
        num_comma = line.count(',')
        num_fullstop = count_endingfullstop(line)
        have_mathoperation = re.search(r'[+−×≤<>≥=≈]+', line)
    
        if (num_comma + num_fullstop) > 0:
            lines.append(line)
        else:
            if not have_mathoperation:
                if is_formula(line):
                    lines.append('[FORMULA]')
                else:
                    lines.append(line)
            else:
                lines.append('[FORMULA]')
    return '\n'.join(lines)


def remove_inline_formula(_str):
    lines = list()
    for line in _str.splitlines():
        have_formula = re.search(formula_pattern, line)
        have_range = re.search(range_pattern, line)
        if have_formula:
            string_noformula = re.sub(formula_pattern, 'zzz', line)
            string_nobracket = re.sub(r'[()]+', '', string_noformula)
            string_noformula = re.sub(formula_pattern, '[FORMULA]', string_nobracket)
            if re.search(expression_pattern, string_noformula):
                string_noformula = re.sub(expression_pattern, '[FORMULA]', string_noformula)
            if have_range:
                string_noformula = re.sub(range_pattern, '[FORMULA]', string_noformula)
            lines.append(string_noformula)
        if have_range:
            lines.append(re.sub(range_pattern, '[FORMULA]', line))
    return '\n'.join(lines)


def join_broken_words(_str):
    return re.sub(r'\b- \b', '', _str)


def mult_to_single_line(_str):
    _str = remove_multiple_whitespace(_str)
    return ' '.join(_str.split('\n')).strip()

def merge_placeholder(_str):
    lines = list()
    for line in _str.splitlines():
        lines.append(re.sub(r'(\[FORMULA\]([,.] ?)?){2,}', '[FORMULA]', line))
    return '\n'.join(lines)


# main function
def Clean(txt, debug=0):
    methods = [
        string_validation,
        remove_formula,
        remove_inline_formula,
        join_broken_words,
        known_replacements,
        remove_non_ascii,
        mult_to_single_line,
        merge_placeholder
    ]
    for m in methods:
        txt = m(txt)
        if debug:
            print('\n\n{}\n\n{}'.format(m, txt))
    return txt
