import re
import keyword
import builtins
from collections import defaultdict

def get_keywords(docx):
    new_string = re.sub(r"\W+", " ", docx)
    return new_string

def get_reserverd_words(docx):
    cleaned_docx = get_keywords(docx)
    reservedword_dict = defaultdict(int)
    identifier_dict = defaultdict(int)
    builtins_dict = defaultdict(int)
    for i in cleaned_docx.split():
        if i in keyword.kwlist:
            reservedword_dict[i] += 1
        elif i in list(dir(builtins)):
            builtins_dict[i] += 1
        else:
            identifier_dict[i] += 1
            
    results = {'reserved': reservedword_dict, "identifiers":identifier_dict,"builtins":builtins_dict}
    return results