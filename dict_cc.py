# Parse the dict.cc data structure 
from rich import print
from pydantic import BaseModel
from typing import Optional, Literal

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
    
def parse_line(line: str) -> DictLine:
    try:
        parts = line.split("\t")
        source = parts[0]
        target = parts[1]
        pos = parts[2]
        tags = parts[3] 
    except: 
        print(line)
        return []
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
    print(list(contents)[0:40])