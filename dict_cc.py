# Parse the dict.cc data structure 
from rich import print
from pydantic import BaseModel
from typing import Optional, Literal
import re

class DictLine(BaseModel):
    source: str 
    target: str
    pos: str
    tags: str
    gender: Optional[Literal["m", "f", "n"]]

def filter_line(line: str) -> bool:
    if line[0] == '#':
        return False
    if line.isspace():
        return False
    return True

def parse_brackets(string: str):
    matches_curly = re.findall(r'\{([^}]*)\}', string)
    cleaned_curly = re.sub(r'\{[^}]*\}', '', string)
    
    matches_square = re.findall(r'\[([^\]]*)\]', cleaned_curly)
    cleaned_square = re.sub(r'\[[^\]]*\]', '', cleaned_curly)
    
    return cleaned_square, matches_curly, matches_square
    
def parse_line(line: str) -> DictLine:
    parts = line.split("\t")
    source = parts[0]
    target = parts[1]
    pos = parts[2]
    tags = parts[3] 

    source, gender, other_tags = parse_brackets(source)
    target, _, _ = parse_brackets(target)
    gender = gender[0] if gender else None
    tags = tags + ",".join(other_tags)
    return DictLine(
        source = source,
        target=target,
        pos=pos,
        tags=tags,
        gender=None
    ) 
    
with open("german_to_english_dict_cc.txt") as dictcc_file:
    contents = dictcc_file.readlines()
    contents = filter(filter_line, contents)
    contents = map(parse_line, contents)
    print(list(contents)[1000:1040])