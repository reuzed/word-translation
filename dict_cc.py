# Parse the dict.cc data structure 
from rich import print
from pydantic import BaseModel
from typing import Optional, Literal
import re

class DictLine(BaseModel):
    source: str 
    target: str
    raw_source: str
    raw_target: str
    pos: str
    tags: str
    genders: list[Literal["m", "f", "n"]]
    curly_tags: list[str]

def filter_line(line: str) -> bool:
    if line[0] == '#':
        return False
    if line.isspace():
        return False
    return True

def parse_square_brackets(string: str):
    matches = re.findall(r'\[([^\]]*)\]', string)
    cleaned = re.sub(r'\[[^\]]*\]', '', string)
    return cleaned, matches
 
def parse_curly_brackets(string: str):
    matches = re.findall(r'\{([^}]*)\}', string)
    cleaned = re.sub(r'\{[^}]*\}', '', string)
    return cleaned, matches

def parse_triangle_brackets(string: str):
    matches = re.findall(r'<([^>]*)>', string)
    cleaned = re.sub(r'<[^>]*>', '', string)
    return cleaned, matches

def parse_round_brackets(string: str):
    matches = re.findall(r'\(([^)]*)\)', string)
    cleaned = re.sub(r'\([^)]*\)', '', string)
    return cleaned, matches

def parse_brackets(string: str):
    cleaned, round_matches = parse_round_brackets(string)
    cleaned, square_matches = parse_square_brackets(cleaned)
    cleaned, triangle_matches = parse_triangle_brackets(cleaned)
    cleaned, curly_matches = parse_curly_brackets(cleaned)
    
    return cleaned,round_matches,square_matches,triangle_matches,curly_matches

def parse_line(line: str) -> DictLine:
    parts = line.split("\t")
    raw_source = parts[0]
    raw_target = parts[1]
    pos = parts[2]
    tags = parts[3] 
    
    source, round_matches, square_matches, triangle_matches, curly_matches = parse_brackets(raw_source)
    
    target, _, _, _, _ = parse_brackets(raw_target)
    genders = list([ct for ct in curly_matches if ct in ['m', 'f', 'n']])
    curly_tags = list([ct for ct in curly_matches if ct not in ['m', 'f', 'n']])
    tags = tags + ",".join(round_matches + square_matches + triangle_matches)
    
    source = source.strip()
    target = target.strip()
    tags = tags.strip()
    
    return DictLine(
        source = source,
        target=target,
        raw_source=raw_source,
        raw_target=raw_target,
        pos=pos,
        tags=tags,
        genders=genders,
        curly_tags=curly_tags,
    ) 
    
with open("german_to_english_dict_cc.txt") as dictcc_file:
    contents = dictcc_file.readlines()
    contents = filter(filter_line, contents)
    dict_lines = map(parse_line, contents)
    simple_dict = dict({
        line.source.lower().strip(): line.target for line in dict_lines
    })
    print(list(simple_dict.values())[2000:2040])

def g_to_e(word: str) -> str:
    return simple_dict.get(word, word)
    