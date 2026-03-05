# Load extracts from /extracts (based on the metadata)

import json
with open("extracts/metadata.json") as meta_file:
    metadata = json.load(meta_file)

def load_extracts() -> dict[str, str]:
    extracts = {}
    for meta in metadata:
        path = meta["file"]
        code = meta["code"]
        start_line, end_line = meta["start_line"], meta["end_line"] 
        with open(path) as f:
            lines = f.readlines()[start_line:end_line]
        extracts[code] = "".join(lines)
    return extracts

def load_extract(code:str, max_lines:int):
    extract = load_extracts()[code]
    return "\n".join(extract.split("\n")[:max_lines])

def list_extract_codes() -> list[str]: 
    codes = []
    for meta in metadata:
        code = meta["code"]
        codes.append(code)
    return codes
    
if __name__ == "__main__":
    print(list_extract_codes())
    
    print(load_extract("maedchen", 30))